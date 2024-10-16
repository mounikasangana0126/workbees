from rest_framework import serializers
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.user_serializer import UserSerializer
from adminmodule.versioned.v1.serializer.department_serializer import DepartmentSerializer
from adminmodule.versioned.v1.serializer.designation_serializer import DesignationSerializer
from adminmodule.versioned.v1.serializer.shift_timings_serializer import ShiftTimeSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    user_data=UserSerializer(source='user',read_only=True)
    department_data=DepartmentSerializer(source='department',read_only=True)
    designation_data=DesignationSerializer(source='designation',read_only=True)
    shift_timings_data=ShiftTimeSerializer(source='employee_shift',read_only=True)
    
    class Meta:
        model=Employees
        fields=['id','employee_id','date_of_birth','profile_pic','emp_is_active','auto_clockout','city','address','joining_date','user_data','employee_shift','designation','department_data','designation_data','shift_timings_data']
        
        