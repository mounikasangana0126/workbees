"""Employee Serializer"""

from rest_framework import serializers
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.user_serializer import UserSerializer
from adminmodule.versioned.v1.serializer.department_serializer import DepartmentSerializer
from adminmodule.versioned.v1.serializer.designation_serializer import DesignationSerializer
from adminmodule.versioned.v1.serializer.shift_timings_serializer import ShiftTimeSerializer
from adminmodule.models.department_head_model import DepartmentHeadModel
from adminmodule.models.designation_model import DesignationModel

class EmployeeSerializer(serializers.ModelSerializer):
    """Employee serializer for employee profile"""
    
    user_data=UserSerializer(source='user',read_only=True)
    department_data=DepartmentSerializer(source='designation.department',read_only=True)
    designation_data=DesignationSerializer(source='designation',read_only=True)
    shift_timings_data=ShiftTimeSerializer(source='employee_shift',read_only=True)
    # reporting_head=serializers.SerializerMethodField()
    
    class Meta:
        """Meta information for Employee"""
        model=Employees
        fields=['id','employee_id','date_of_birth','profile_pic','emp_is_active','auto_clockout','city','address','joining_date','user_data','employee_shift','designation','department_data','designation_data','shift_timings_data']
    
    # def get_reporting_head(self, obj):
    #     department=DesignationModel.objects.filter(id=obj.designation).first()

    #     if department:
    #         reporting_head=DepartmentHeadModel.objects.filter(department=department.id).first()
    #         return reporting_head if reporting_head else None
    #     return None
            