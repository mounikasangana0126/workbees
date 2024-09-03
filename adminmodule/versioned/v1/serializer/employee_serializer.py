from rest_framework import serializers
from adminmodule.models.employee_model import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'