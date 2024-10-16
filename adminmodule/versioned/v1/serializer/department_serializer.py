from rest_framework import serializers
from adminmodule.models.department_model import DepartmentModel, ParentModel

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = ["id", "parent_dept"]  

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepartmentModel
        fields = ["id","dept_name","parent","dept_is_enabled"]
 