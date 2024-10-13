from rest_framework import serializers
from adminmodule.models.employee_model import Employees
from adminmodule.models.department_model import DepartmentModel
from adminmodule.models.designation_model import DesignationModel

class EmployeeSerializer(serializers.ModelSerializer):
    department=serializers.StringRelatedField()
    designation=serializers.StringRelatedField()
    class Meta:
        model = Employees
        fields = '__all__'