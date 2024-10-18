from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.time_entry_serializer import TimeEntrySerializer
from adminmodule.versioned.v1.serializer.check_in_check_out_serializer import CheckinCheckoutSerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

class CheckInCheckOutAPI(APIView):
    """CheckInCheckOut API"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Handle GET request and return all employees' time entries and break entries."""
        data = TimeEntry.objects.filter(employee__user=request.user)

        if not data.exists():
            return Response({
                'message': 'No employees with time entries or break entries found',
                'data': []  
            }, status=status.HTTP_204_NO_CONTENT)
        
        serializer = CheckinCheckoutSerializer(data, many=True)
        return Response({
            'message': 'Fetched all employees\' time entries and break entries',
            'data': serializer.data  
        }, status=status.HTTP_200_OK)

    def get(self, request, id):
        """Handle GET request to retrieve all time entries of a specific employee."""
        
        try:
            queryset = TimeEntry.objects.get(id=id)

            if not queryset.DoesNotExist:
                return Response({
                    'message': 'Employee time entry details not found',
                    'data': []  
                }, status=status.HTTP_404_NOT_FOUND)

        except Employees.DoesNotExist:
            return Response({
                'message': 'Employee not found',
                'data': []  
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CheckinCheckoutSerializer(queryset)
        return Response({
            'message': 'Time entries of the employee retrieved successfully',
            'data': serializer.data 
        }, status=status.HTTP_200_OK)

class CheckInDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Handle POST request to add a new time entry for an employee."""
        now=timezone.localtime()
        current_date=now.strftime("%Y-%m-%d")
        current_time=now.strftime("%H:%M:%S")
        if not TimeEntry.objects.filter(employee__user=request.user, date=current_date).exists():
            employee=Employees.objects.get(user=request.user)
            employee_id=employee.id
            time_entry_data = {
                'clock_in': current_time,
                'date': current_date,  
                'employee': employee_id
            }

            serializer = CheckinCheckoutSerializer(data=time_entry_data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Clock-in added successfully.',
                    'data': serializer.data  
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                'message': 'Invalid data',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'message': 'Already clocked in',
            'data': [],
        }, status=status.HTTP_400_BAD_REQUEST)


class CheckOutDetailAPI(APIView):
    permission_classes = [IsAuthenticated]
    pass

    

   