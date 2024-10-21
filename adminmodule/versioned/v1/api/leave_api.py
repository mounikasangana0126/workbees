from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adminmodule.models.leave_model import Leave
from adminmodule.versioned.v1.serializer.leave_serializer import LeaveSerializer 
from adminmodule.versioned.v1.serializer.leave_serializer import Employee # Fixed the import name to EmployeeSerializer
from adminmodule.models.employee_model import Employees
from rest_framework.permissions import IsAuthenticated

# API to handle leave records for employees
class LeaveAPI(APIView):
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def get(self, request):
        """Handle GET request to fetch all leave records of the authenticated employee."""
        # Fetch the employee linked to the authenticated user
        query = Employees.objects.filter(user=request.user)
        
        if not query.exists():  # Check if the employee exists
            return Response({
                'message': 'No employee records found for the authenticated user.',
                'data': [],  # Return empty data
                'status': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Employee(query, many=True)  # Serialize the employee records
        return Response({
            'message': 'Leave records of the employee fetched successfully',
            'data': serializer.data,  # Return serialized data
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Handle POST request to add a leave record for the authenticated employee."""
        serializer = LeaveSerializer(data=request.data)  # Initialize serializer with request data
        
        try:
            employee = Employees.objects.get(user=request.user)  # Get the employee linked to the authenticated user
        except Employees.DoesNotExist:
            return Response({
                'message': 'Employee not found for the authenticated user.',
                'data': None,
                'status': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():  # Check if the serializer data is valid
            serializer.save(employee=employee)  # Save the leave record linked to the employee
            return Response({
                'message': 'Leave request sent successfully',
                'data': serializer.data,  # Return the serialized leave record
                'status': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'message': 'Invalid data provided',
            'errors': serializer.errors,  # Return validation errors
            'status': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)

# API to handle individual leave record operations
class LeaveDetailAPI(APIView):
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def get(self, request, id):
        """Handle GET request to get a particular leave record of the authenticated employee."""
        try:
            snippet = Leave.objects.get(id=id)  # Fetch the leave record by ID
        except Leave.DoesNotExist:
            return Response({
                'message': 'Leave record not found',
                'data': None,
                'status': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LeaveSerializer(snippet)  # Serialize the leave record
        return Response({
            'message': 'Leave record fetched successfully',
            'data': serializer.data,  # Return serialized data
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
