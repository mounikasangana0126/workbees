from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.time_entry_serializer import TimeEntrySerializer
from adminmodule.versioned.v1.serializer.check_in_check_out_serializer import EmployeeCheckInCheckOut
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

class CheckInCheckOutAPI(APIView):
    """CheckInCheckOut API"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Handle GET request and return all employees' time entries and break entries."""
        
        # Fetch all employee records
        data = Employees.objects.all()

        # Check if there are no employees with time or break entries
        if not data.exists():
            return Response({
                'message': 'No employees with time entries or break entries found',
                'data': []  # Send empty data in response for no records
            }, status=status.HTTP_204_NO_CONTENT)
        
        # Serialize employee data with related time entries and break entries
        serializer = EmployeeCheckInCheckOut(data, many=True)
        return Response({
            'message': 'Fetched all employees\' time entries and break entries',
            'data': serializer.data  # Return the serialized data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """Handle POST request to add a new time entry for an employee."""
        
        # Initialize serializer with incoming data
        serializer = TimeEntrySerializer(data=request.data)
        
        # Fetch the employee record using the provided employee ID
        employee = Employees.objects.get(id=request.data.get('employee'))
        
        # Validate serializer data and save new time entry
        if serializer.is_valid():
            serializer.save(employee=employee)
            return Response({
                'message': 'Clock-in added successfully.',
                'data': serializer.data  # Return the newly created entry
            }, status=status.HTTP_201_CREATED)
        
        # If data is invalid, return validation errors
        return Response({
            'message': 'Invalid data',
            'data': serializer.errors  # Provide details about the validation errors
        }, status=status.HTTP_400_BAD_REQUEST)


class CheckInCheckOutDetailsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        """Handle GET request to retrieve all time entries of a specific employee."""
        
        try:
            # Filter for employee's time entry details using their ID
            queryset = Employees.objects.filter(id=id)

            # Check if employee record is found
            if not queryset.exists():
                return Response({
                    'message': 'Employee time entry details not found',
                    'data': []  # Send empty data in response if not found
                }, status=status.HTTP_404_NOT_FOUND)

        except Employees.DoesNotExist:
            # Handle the case where the employee does not exist
            return Response({
                'message': 'Employee not found',
                'data': []  # Send empty data if the employee doesn't exist
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Serialize the filtered employee's time entry data
        serializer = EmployeeCheckInCheckOut(queryset, many=True)
        return Response({
            'message': 'Time entries of the employee retrieved successfully',
            'data': serializer.data  # Return the serialized data
        }, status=status.HTTP_200_OK)

    def put(self, request, id):
        """Handle PUT request to update time entry details by time entry ID."""
        
        try:
            # Filter for the time entry by its ID
            queryset = TimeEntry.objects.filter(id=id)

            # Check if the time entry exists
            if not queryset.exists():
                return Response({
                    'message': 'Time entry not found for the given ID',
                    'data': []  # Return empty data if not found
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Fetch the user details from the request
            user_id = request.user.id
            user = User.objects.get(id=user_id)
        
        except User.DoesNotExist:
            # Handle case where the user does not exist
            return Response({
                'message': 'User not found',
                'data': []  # Send empty data in case of a missing user
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Initialize serializer with the existing time entry and new data
        serializer = TimeEntrySerializer(instance=queryset.first(), data=request.data, partial=True)
        
        # Validate and save the updated data
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Time entry details updated successfully',
                'data': serializer.data  # Return updated time entry details
            }, status=status.HTTP_200_OK)
        
        # Return validation errors if data is invalid
        return Response({
            'message': 'Invalid data',
            'data': serializer.errors  # Provide details of the errors
        }, status=status.HTTP_400_BAD_REQUEST)
