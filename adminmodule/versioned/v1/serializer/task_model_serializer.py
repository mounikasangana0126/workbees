from rest_framework import serializers
from adminmodule.models.task_model import Task
class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
        
