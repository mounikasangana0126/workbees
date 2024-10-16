from rest_framework import serializers
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer import user_serializer
from adminmodule.versioned.v1.serializer import department_serializer
from adminmodule.versioned.v1.serializer import designation_serializer
from adminmodule.versioned.v1.serializer import shift_timings_serializer

class EmployeeSeializer(serializers.ModelSerializer):
    user=user_serializer()
    Department=department_serializer()
    Designation=designation_serializer()
    shift=shift_timings_serializer()
    
    class Meta:
        model=Employees
        fields=['user','id','joining_date','employee_shift','profile_pic','employee_id','Department','Designation','designation','shift','date_of_birth','employee_id','emp_is_active','auto_clockout','city','address',]
        
        