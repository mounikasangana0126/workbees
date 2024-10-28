"""Employee Task API.""" 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from adminmodule.models.task_model import Task
from adminmodule.versioned.v1.serializer.task_model_serializer import TaskSerializer

class TaskEmployeeAPI(APIView):
    """API for employees to view and update their assigned tasks."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get tasks assigned to the authenticated employee.
        """
        employee = request.user.employees
        tasks = Task.objects.filter(assigned_to=employee)
        serializer = TaskSerializer(tasks, many=True)
        return Response(
            {
                "message": "Tasks fetched successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, id=None):
        """
        Update a task assigned to the authenticated employee.
        """
        employee = request.user.employees
        try:
            task = Task.objects.get(id=id, assigned_to=employee)
        except Task.DoesNotExist:
            return Response(
                {
                    "message": "Task not found or you are not authorized to update this task",
                    "data": []
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Task updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                "message": "Failed to update task",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
