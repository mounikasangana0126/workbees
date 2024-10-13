from rest_framework import serializers
from adminmodule.models.leave_model import Leave
from adminmodule.models.employee_model import Employees


class LeaveSerializer(serializers.ModelSerializer):
    employees=serializers.StringRelatedField()
    class Meta:
        model=Leave
        fields='__all__'