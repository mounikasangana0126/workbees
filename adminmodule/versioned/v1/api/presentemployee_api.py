from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import date

from utils.helper.permission import SuperuserPermission 

from adminmodule.models.department_model import DepartmentModel
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees

from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer
from adminmodule.versioned.v1.serializer.time_entry_serializer import EmployeePresentSerializer,EmployeeAsentSerializer


class PresentEmployeeGetAPI(APIView):
    """ Present and Absent Employee details."""
    permission_classes = [SuperuserPermission]
    
    def get(self, request, id):
        """ Handle Get request and return response."""
        
        department_present_employee = TimeEntry.objects.filter(
            employee__designation__department__id = id,
            clock_in__date = timezone.now().date()
        )
        serializer = EmployeePresentSerializer(department_present_employee, many = True)
        return Response(
            {
                'message': 'Today employee present for a particular department data fetched',
                'data':serializer.data,
                'total_count':department_present_employee.count()
            },
            status=status.HTTP_200_OK
        )
class AbsentEmployeeGetAPI(APIView):
    """ Absent Employee details"""
    
    def get(self, request, id):
        """ Handle Get request and return response."""
        
        department_all_employees = Employees.objects.filter(
            designation__department__id = id
        )
        
        department_absent_employees = department_all_employees.exclude(
            timeentry__clock_in__date = timezone.now().date()
        )
        serializer = EmployeeAsentSerializer(department_absent_employees, many = True)
        return Response(
            {
                'message':'Today employee absent for a particular department data fetch',
                'data':serializer.data,
                'total_count':department_absent_employees.count()
            },
            status=status.HTTP_200_OK
        )
        
        
        
        
        