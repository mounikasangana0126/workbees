from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User  # Import the User model
from rest_framework import status
from adminmodule.models.employee_model import Employees  # Import Employees model
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer  # Import EmployeeSerializer
from utils.helper.permission import SuperuserPermission  # Custom permission for superusers

# API to handle employee-related operations for admins
class EmployeeGetAdminAPI(APIView):
    permission_classes = [SuperuserPermission]  # Restrict access to superusers only
    
    # GET method to retrieve all employees
    def get(self, request):
        """Handle GET request and return all employees"""
        queryset = Employees.objects.all()  # Fetch all employee records
        serializer = EmployeeSerializer(queryset, many=True)  # Serialize multiple records
        
        # Return response with message and serialized data
        return Response({
            "message": "Employees fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # POST method to create a new employee
    def post(self, request):
        """Handle POST request to create a new employee"""
        serializer = EmployeeSerializer(data=request.data)  # Initialize serializer with request data
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save the new employee record
            return Response({
                "message": "Employee created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        # Return error response if data is invalid
        return Response({
            "message": "Invalid data provided",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

# API to handle operations on individual employee records (view, update, delete)
class EmployeeGetAdminDetailAPI(APIView):
    permission_classes = [SuperuserPermission]  # Restrict access to superusers only

    # GET method to retrieve a specific employee by their ID
    def get(self, request, id):
        """Handle GET request and return a specific employee by their ID"""
        try:
            snippet = Employees.objects.get(id=id)  # Fetch the employee record by ID
        except Employees.DoesNotExist:
            return Response({
                "message": "Employee not found",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(snippet)  # Serialize the employee record
        return Response({
            "message": "Employee fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # PUT method to update a specific employee by their ID
    def put(self, request, id):
        """Handle PUT request to update a specific employee"""
        try:
            queryset = Employees.objects.get(id=id)  # Fetch the employee record by ID
        except Employees.DoesNotExist:
            return Response({
                "message": "Employee not found",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Update the employee record with new data
        serializer = EmployeeSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save the updated employee record
            return Response({
                "message": "Employee updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        # Return error response if data is invalid
        return Response({
            "message": "Invalid data provided",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete a specific employee by their ID
    def delete(self, request, id):
        """Handle DELETE request to remove a specific employee"""
        try:
            queryset = Employees.objects.get(id=id)  # Fetch the employee record by ID
        except Employees.DoesNotExist:
            return Response({
                "message": "Employee not found",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the employee record
        queryset.delete()
        return Response({
            "message": "Employee deleted successfully",
            "data": None
        }, status=status.HTTP_204_NO_CONTENT)
