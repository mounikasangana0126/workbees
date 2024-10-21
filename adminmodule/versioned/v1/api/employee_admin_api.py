"""Employee admin api."""

from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User  
from rest_framework import status
from adminmodule.models.employee_model import Employees  
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer
from utils.helper.permission import SuperuserPermission  
from adminmodule.models.designation_model import DesignationModel
from adminmodule.models.shift_timings_model import WorkShiftsModel
class EmployeeGetAdminAPI(APIView):
    """API View to fetch and create employee records for admins."""
    permission_classes = [SuperuserPermission]  
    
    def get(self, request):
        """Handle GET request and return all employees."""

        queryset = Employees.objects.all() 
        serializer = EmployeeSerializer(queryset, many=True)  
        return Response(
            {
                "message": "Employees fetched successfully",
                "data": serializer.data if serializer.data else []
            }, 
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """Handle POST request to create a new employee."""
        data=request.data
        # user=User.objects.get(username=data["username"])
        # designation=DesignationModel.objects.get(designation_name=data["designation_name"])
        # shift_name=WorkShiftsModel.objects.get(shift_name=data["shift_name"])
        # data["user"]=user
        # data["designation"]=designation.id
        # data["employee_shift"]=shift_name.id
        serializer = EmployeeSerializer(data=data) 
        if serializer.is_valid():  
            serializer.save() 
            return Response(
                {
                    "message": "Employee created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "message": "Invalid data provided",
                "errors": serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )


class EmployeeGetAdminDetailAPI(APIView):
    """API View to handle individual employee records for admins."""
    permission_classes = [SuperuserPermission]  

    def get(self, request, id):
        """Handle GET request and return a specific employee by their ID."""

        try:
            snippet = Employees.objects.get(id=id) 
        except Employees.DoesNotExist:
            return Response(
                {
                    "message": "Employee not found",
                    "data": []
                }, 
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EmployeeSerializer(snippet)
        return Response(
            {
                "message": "Employee fetched successfully",
                "data": serializer.data if serializer.data else []
            }, 
            status=status.HTTP_200_OK
        )

    def put(self, request, id):
        """Handle PUT request to update a specific employee."""

        try:
            queryset = Employees.objects.get(id=id)  
        except Employees.DoesNotExist:
            return Response(
                {
                    "message": "Employee not found",
                    "data": []
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = EmployeeSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():  
            serializer.save()  
            return Response(
                {
                    "message": "Employee updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        
        return Response(
            {
                "message": "Invalid data provided",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        """Handle DELETE request to remove a specific employee."""
        
        try:
            queryset = Employees.objects.get(id=id)  
        except Employees.DoesNotExist:
            return Response(
                {
                    "message": "Employee not found",
                    "data": []
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        queryset.delete()
        return Response(
            {
                "message": "Employee deleted successfully",
                "data": []
            }, 
            status=status.HTTP_204_NO_CONTENT
        )
