"""leave serializer"""

from rest_framework import serializers
from adminmodule.models.leave_model import Leave
from adminmodule.models.employee_model import Employees
from adminmodule.models.designation_model import DesignationModel
from datetime import date

class Employee(serializers.ModelSerializer):
    """"Employee Serializer"""
    designation=serializers.StringRelatedField()
    class Meta:
        """Meta information for employee."""
        model = Employees
        fields = ['employee_id','designation',]
class GetLeaveSerializer(serializers.ModelSerializer):
    """Serializer for the Leave model."""
    employee=Employee()
    class Meta:
        model=Leave
        fields=['employee','id','start_date', 'end_date', 'leave_type', 'leave_shift', 'reason', 'status', 'total_days']

class PostLeaveSerializer(serializers.ModelSerializer):
    """Serializer for the Leave model."""
    class Meta:
        model=Leave
        fields=['start_date', 'end_date', 'leave_type', 'reason', 'status', 'leave_shift']
    
    def validate(self, data):
        """Validate that start_date is not in the past."""
        if data['start_date'] < date.today():
            raise serializers.ValidationError("Start date cannot be in the past.")
        if data['end_date']< data['start_date']:
            raise serializers.ValidationError("End date cannot be before start date.")
        return data
class AdminLeavePostSerializer(serializers.ModelSerializer):
    employee_ids=serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all(),many=True,write_only=True)
    class Meta:
        model=Leave
        fields=['start_date', 'end_date', 'leave_type', 'leave_shift', 'reason', 'employee_ids']
    def create(self,validated_data):
        employee_ids=validated_data.pop('employee_ids')
        for employee in employee_ids:
            leave = Leave.objects.create(employee=employee, **validated_data)
        return leave