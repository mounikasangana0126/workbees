from rest_framework import serializers
from adminmodule.models.employee_model import Employees
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=['emp_is_active']
        