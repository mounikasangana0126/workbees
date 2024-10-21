"""Department and Parent serializer."""

from rest_framework import serializers
from adminmodule.models.department_model import DepartmentModel, ParentModel

class ParentSerializer(serializers.ModelSerializer):
    """Parent serializer."""
    class Meta:
        model = ParentModel
        fields = ["id", "parent_dept"]  

class DepartmentSerializer(serializers.ModelSerializer):
    """Department serializer."""
    class Meta:
        model = DepartmentModel
        fields = ["id","dept_name","parent","dept_is_enabled"]
 