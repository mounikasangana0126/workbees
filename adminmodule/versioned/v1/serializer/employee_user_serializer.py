from rest_framework import serializers
from adminmodule.models.employee_model import Employees
from adminmodule.models.user_model import User
class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['name','username','phone_number']
class EmployeeSeializer1(serializers.ModelSerializer):
    user=UserSerializer1()
    class Meta:
        model=Employees
        fields=['employee_id','designation','user']

    