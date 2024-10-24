"""Task Admin API."""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from adminmodule.models.task_model import Task
from adminmodule.versioned.v1.serializer.task_model_serializer import TaskSerializer
from utils.helper.permission import SuperuserPermission
from rest_framework.permissions import IsAuthenticated

class TaskAdminAPI(APIView):
    """API for admin to handle tasks."""
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        """Get all tasks."""
        if request.user.is_admin==True:
            """Get all tasks if user is admin."""

            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True) 
            return Response(
                {
                    "message": "Data fetched successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

    def post(self, request):
        """Create a new task and assign it to employees."""

        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Task created and assigned to employees successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'message': 'Failed to create task',
                'errors': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class TaskAdminDetailsAPI(APIView):
    """API for admin to handle a specific task."""

    def get(self, request, id):
        """Get task details by ID."""
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response(
                {
                    "message": "Task not found",
                    "data": []
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TaskSerializer(task)
        return Response(
            {
                "message": "Data fetched successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def put(self, request, id):
        """Update task details by ID."""
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response(
                {
                    "message": "Task not found",
                    "data": []
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
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

    def delete(self, request, id):
        """Delete task by ID."""
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response(
                {
                    "message": "Task not found",
                    "data": []
                },
                status=status.HTTP_404_NOT_FOUND
            )
        task.delete()
        return Response(
            {
                "message": "Task deleted successfully"
            },
            status=status.HTTP_200_OK
        )
