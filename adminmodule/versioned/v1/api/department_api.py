"""Parent and Department API."""

from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.department_model import DepartmentModel, ParentModel
from adminmodule.versioned.v1.serializer.department_serializer import DepartmentSerializer, ParentSerializer
from rest_framework import status
from utils.helper.permission import SuperuserPermission
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees
from django.utils import timezone
from adminmodule.models.leave_model import Leave

class ParentGetAPI(APIView):
    """Parent Get API View."""
    permission_classes=[SuperuserPermission]
    
    def get(self, request):
        """Handle GET requests and return response."""
        queryset = ParentModel.objects.all()
        serializer = ParentSerializer(queryset, many=True)
        return Response(
            {
                "message": "Parent fetched successfully.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

class DepartmentGetAPI(APIView):
    """Department Get API View."""
    permission_classes=[SuperuserPermission]

    def get(self, request):
        """Handle GET requests and return response."""
        
        queryset = DepartmentModel.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        present_employee = TimeEntry.objects.filter(clock_in__date = timezone.now().date()).count()
        all_employee = Employees.objects.filter(emp_is_active = True).count()
        total_absents = all_employee - present_employee
        leave_requests = Leave.objects.filter(status = 'PENDING').count()
        return Response({
            "messege":"Departments fetched successfully",
            "all_employee":all_employee,
            "present_employee":present_employee,
            "total_absents":total_absents,
            "leave_requests": leave_requests,
            "data": serializer.data
            },
            status= status.HTTP_200_OK
        )
        
    def post(self, request):
        """Handle POST requests and save the request data."""
        data=request.data
        Parent=ParentModel.objects.get(parent_dept=data["parent"])
        data["parent"]=Parent.id
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentGetDetailAPI(APIView):
    """Department Detail API View."""
    permission_classes=[SuperuserPermission]
    def get(self, request, id):
        """Retrieve a specific department by ID."""
        try:
            department = DepartmentModel.objects.get(id=id)
            serializer = DepartmentSerializer(department)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DepartmentModel.DoesNotExist:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        """Handle PATCH requests and update the department."""
        try:
            queryset = DepartmentModel.objects.get(id=id)
        except DepartmentModel.DoesNotExist:
            return Response({'error': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DepartmentSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Handle DELETE requests and delete data from department model."""
        
        try:
            queryset = DepartmentModel.objects.get(id=id)
        except:
            return Response({"error":"queryset not found"}, status= status.HTTP_400_BAD_REQUEST)
        
        queryset.delete()
        return Response({"message":"Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
