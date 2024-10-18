from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User  
from rest_framework import status
from adminmodule.models.employee_model import Employees 
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer  
from rest_framework.permissions import IsAuthenticated 

class EmployeeGetAPI(APIView):
    """API View to handle employee-related requests for authenticated users."""
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        """Handle GET request to fetch employee details."""
        snippet = Employees.objects.filter(user=request.user)  
        serializer = EmployeeSerializer(snippet, many=True) 
        
        return Response({
            "message": "Employee details fetched successfully",
            "data": serializer.data if serializer.data else []  
        }, status=status.HTTP_200_OK)

    def put(self, request):
        """Handle PATCH request to update employee data."""
        queryset = Employees.objects.filter(user=request.user) 
        
        if not queryset.exists():  
            return Response({
                "message": "No employee records found for this user",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(queryset, data=request.data, partial=True)  
        
        if serializer.is_valid():  
            serializer.save() 
            return Response({
                "message": "Employee details updated successfully",
                "data": serializer.data  
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Invalid data provided",
            "errors": serializer.errors  
        }, status=status.HTTP_400_BAD_REQUEST)
