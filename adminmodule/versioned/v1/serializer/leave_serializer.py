"""leave serializer"""
from rest_framework import serializers
from adminmodule.models.leave_model import Leave
from adminmodule.models.employee_model import Employees


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leave
        fields=['id','start_date', 'end_date', 'leave_type','reason','status','total_days']
        
class Employee(serializers.ModelSerializer):
    leave_records = LeaveSerializer(many = True)
    class Meta:
        model = Employees
        fields = ['id', 'employee_id','designation', 'leave_records']