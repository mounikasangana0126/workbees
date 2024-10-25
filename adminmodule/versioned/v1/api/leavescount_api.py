from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from adminmodule.models.leave_model import Leave
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees

from rest_framework.permissions import IsAuthenticated 

from adminmodule.versioned.v1.serializer.leave_serializer import GetLeaveSerializer


class LeavesCountGetAPI(APIView):
    """ Leave Count Class."""
    
    permission_classes = [IsAuthenticated]
    def get(self, request):
        """ Handle Get request and return response."""
        
        employee = Employees.objects.get(user = request.user.id)
        timee = timezone.now()
        sick_leaves = Leave.objects.filter(employee = employee, leave_type = 'SICK', start_date__year = timee.year, status = 'APPROVED')
        casual_leaves = Leave.objects.filter(employee = employee, leave_type = 'CASUAL', start_date__year = timee.year, status = 'APPROVED')
        other_leaves = Leave.objects.filter(employee= employee,  start_date__year = timee.year, status = 'APPROVED').exclude(leave_type__in=['SICK', 'CASUAL'])
        
        work_from_home = TimeEntry.objects.filter(employee = employee, work_mode = 'WFH', date__month = timee.month).count()
        work_from_office = TimeEntry.objects.filter(employee = employee, work_mode = 'WFO', date__month = timee.month).count()
        monthly_leaves = Leave.objects.filter(employee = employee, status = 'APPROVED', start_date__month = timee.month)
        
        sick_leaves_data = GetLeaveSerializer(sick_leaves, many=True).data
        casual_leaves_data = GetLeaveSerializer(casual_leaves, many=True).data
        other_leaves_data = GetLeaveSerializer(other_leaves, many=True).data
        monthly_leaves_data = GetLeaveSerializer(monthly_leaves, many = True).data
        

        
        sick_leave_count = 0
        casual_leaves_count = 0
        other_leaves_count = 0
        monthly_leaves_count = 0
        
        for leave in sick_leaves_data:
            sick_leave_count = sick_leave_count + leave['total_days']
        for leave in casual_leaves_data:
            casual_leaves_count = casual_leaves_count + leave['total_days']
        for leave in other_leaves_data:
            other_leaves_count = other_leaves_count + leave['total_days']
        for leave in monthly_leaves_data:
            monthly_leaves_count = monthly_leaves_count + leave['total_days']
        
        return Response(
            {
                'message':'Leaves count fetched successfully',
                'sick_leaves':sick_leave_count,
                'casual_leaves':casual_leaves_count,
                'other_leaves':other_leaves_count,
                'work_from_home':work_from_home,
                'work_from_office':work_from_office,
                'montly_leaves':monthly_leaves_count
            },
            status=status.HTTP_200_OK
        )
        return None
        