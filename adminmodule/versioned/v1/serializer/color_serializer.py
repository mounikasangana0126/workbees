from rest_framework import serializers
from adminmodule.models.employee_model import Employees

class colorSerializer(serializers.ModelSerializer):
    class Meta():
        model=Employees
        fiels='__all__'
