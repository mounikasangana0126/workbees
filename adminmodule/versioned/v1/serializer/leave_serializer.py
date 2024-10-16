"""leave serializer"""
from rest_framework import serializers
from adminmodule.models.leave_model import Leave
from adminmodule.models.employee_model import Employees


class LeaveSerializer(serializers.ModelSerializer):
    employees=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Leave
        fields=['start_date', 'end_date', 'leave_shift','leave_type','reason','status','total_days','employees']