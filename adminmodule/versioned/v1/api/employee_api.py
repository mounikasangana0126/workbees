from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User  # Import User model
from rest_framework import status
from adminmodule.models.employee_model import Employees  # Import Employees model
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer  # Import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated  # Import authentication permission

class EmployeeGetAPI(APIView):
    """API View to handle employee-related requests for authenticated users."""
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def get(self, request):
        """Handle GET request to fetch employee details."""
        snippet = Employees.objects.filter(user=request.user)  # Fetch employee records associated with the authenticated user
        serializer = EmployeeSerializer(snippet, many=True)  # Serialize the employee records
        
        return Response({
            "message": "Employee details fetched successfully",
            "data": serializer.data if serializer.data else []  # Return an empty list if no data
        }, status=status.HTTP_200_OK)

    def put(self, request):
        """Handle PATCH request to update employee data."""
        queryset = Employees.objects.filter(user=request.user)  # Fetch employee records associated with the authenticated user
        
        if not queryset.exists():  # Check if any records exist
            return Response({
                "message": "No employee records found for this user",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(queryset, data=request.data, partial=True)  # Initialize serializer with request data
        
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save the updated employee record
            return Response({
                "message": "Employee details updated successfully",
                "data": serializer.data  # Return the updated employee data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Invalid data provided",
            "errors": serializer.errors  # Return validation errors
        }, status=status.HTTP_400_BAD_REQUEST)
