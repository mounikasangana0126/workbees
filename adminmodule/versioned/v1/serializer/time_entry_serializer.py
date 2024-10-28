from rest_framework import serializers
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.user_model import User
from adminmodule.models.employee_model import Employees
from adminmodule.models.designation_model import DesignationModel
from adminmodule.models.department_model import DepartmentModel
from adminmodule.versioned.v1.serializer.breakentry_serializer import BreakEntrySerializer
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer
from django.utils import timezone
from datetime import datetime, date
class TimeEntrySerializer(serializers.ModelSerializer):
    """ Time entry serializer."""
    
    breaks = BreakEntrySerializer(many = True, read_only = True)
    class Meta:
        model = TimeEntry
        fields = ['employee','id','clock_in','clock_out','date','work_mode','is_completed','total_work_time','breaks']
        
 
class EmployeePresentSerializer(serializers.ModelSerializer):
    """ Employee present serializer."""
    
    name = serializers.CharField(source = 'employee.user.name', read_only = True)
    username = serializers.CharField(source = 'employee.user.username', read_only = True)
    department= serializers.UUIDField(source = 'employee.designation.department', read_only = True)
    employee_id = serializers.CharField(source = 'employee.employee_id', read_only = True)
    profile_pic = serializers.ImageField(source = 'employee.profile_pic', read_only = True)
    
    class Meta:
        model = TimeEntry
        fields = ['name','username','employee_id','profile_pic','department','clock_in','clock_out']
        
class EmployeeAsentSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(source = 'user.name', read_only = True)
    username = serializers.CharField(source = 'user.username', read_only = True)
    class Meta:
        model = Employees
        fields = ['name','username','profile_pic','employee_id']
        





