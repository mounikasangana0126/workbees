"""Employee Task API.""" 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from adminmodule.models.task_model import Task, TaskEmployeeModel
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.task_model_serializer import TaskSerializer, TaskEmployeeSerializer

class TaskEmployeeAPI(APIView):
    """API for employees to view and update their assigned tasks."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get tasks assigned to the authenticated employee.
        """
        employee = request.user.employees
        tasks = TaskEmployeeModel.objects.filter(employee=employee)
        serializer = TaskEmployeeSerializer(tasks, many=True)
        return Response(
            {
                "message": "Tasks fetched successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
class TaskEmployeeDetailsAPI(APIView):
    def get(self,request,id):
        """
        Get details of a specific task assigned to the authenticated employee.
        """
        employee = request.user
        employee = Employees.objects.get(user__name = employee)
        try:
            task = TaskEmployeeModel.objects.get(id=id, employee=employee.id)
        except TaskEmployeeModel.DoesNotExist:
            return Response(
                {
                    "message": "Task not found or you are not authorized to view this task",
                    "data": []
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = TaskEmployeeSerializer(task)
        return Response(
            {
                "message": "Task fetched successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    def put(self, request, id):
        """
        Update a task assigned to the authenticated employee.
        """
        employee = request.user
        employee = Employees.objects.get(user__name = employee)
        try:
            task = TaskEmployeeModel.objects.get(id=id, employee=employee.id)
        except TaskEmployeeModel.DoesNotExist:
            return Response(
                {
                    "message": "Task not found or you are not authorized to update this task",
                    "data": []
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
        serializer = TaskEmployeeSerializer(task, data=request.data, partial=True)
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
