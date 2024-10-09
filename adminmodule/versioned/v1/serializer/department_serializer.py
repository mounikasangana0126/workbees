from rest_framework import serializers
from adminmodule.models.department_model import DepartmentModel, ParentModel

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source='parent.parent_dept', read_only=True)
    parent = serializers.PrimaryKeyRelatedField(queryset=ParentModel.objects.all(), required=False, allow_null=True)

    class Meta:
        model = DepartmentModel
        fields = ['id', 'dept_name', 'parent', 'parent_name', 'dept_is_enabled']
