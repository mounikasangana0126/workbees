from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from utils.helper.permission import SuperuserPermission

from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees
from adminmodule.models.task_model import Task
from adminmodule.versioned.v1.serializer.time_entry_serializer import EmployeePresentSerializer
# from adminmodule.versioned.v1.serializer.task_model_serializer import TaskSerializer


class RecentLoginEmployeeGetAPI(APIView):
    """ Recent login employees details."""
    
    permission_classes = [SuperuserPermission]
    def get(self, request):
        """ Handle Get request and return response."""
        
        recent_logins = TimeEntry.objects.filter(clock_in__date = timezone.now().date())
        if not recent_logins:
            return Response(
                {
                    'message':'No recent logins',
                    'data':[]
                },
                status=status.HTTP_204_NO_CONTENT
            )
        all_employees = Employees.objects.all().count()
        present_employees = TimeEntry.objects.filter(clock_in__date = timezone.now().date()).count()
        total_present_percentage = (present_employees/all_employees)*100
        serializer = EmployeePresentSerializer(recent_logins, many = True)
        return Response(
            {
                'message':' Recent logins.',
                'all_employees':all_employees,
                'present_employees':present_employees,
                'total_present_percentage': total_present_percentage,
                'data':serializer.data
            },
            status = status.HTTP_200_OK
        )
        
class GetSingleDayLoginsTask(APIView):
    """ Get a particular day presents, logings and tasks.."""
    
    def get(self, request, date):
        """ Handle Get request and return response."""
        
        if not date:
            return Response(
                {
                    'message':'Date is required.',
                    'data':date
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            date = timezone.datetime.strptime(date, '%Y-%m-%d').date()
        except:
            return Response(
                {
                    'message':'Invalid date format',
                    'data':date
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        all_logins = TimeEntry.objects.filter(clock_in__date = date)
        login_serializer = EmployeePresentSerializer(all_logins, many = True)
        all_tasks = Task.objects.filter(created_at__date = date)
        # task_serializer = TaskSerializer(all_tasks, many = True)
        return Response(
            {
                'message':'ALL Logins and tasks for a particular date.',
                'login_data':login_serializer.data,
                # 'task_data': task_serializer.data
            },
            status = status.HTTP_200_OK
        )
        