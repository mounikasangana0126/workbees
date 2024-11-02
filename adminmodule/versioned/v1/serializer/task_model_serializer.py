"""Task serializer."""

from rest_framework import serializers
from adminmodule.models.task_model import Task, TaskEmployeeModel
from adminmodule.models.employee_model import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for the Employees model."""
    class Meta:
        model = Employees
        fields = ['id', 'employee_id', 'profile_pic']

class TaskEmployeeSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    task_id = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), write_only=True)

    class Meta:
        model = TaskEmployeeModel
        fields = ['id', 'employee', 'task_id', 'status']

class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""

    assigned_to = serializers.SerializerMethodField()
    assigned_to_ids = serializers.PrimaryKeyRelatedField(queryset=Employees.objects.all(), many=True, write_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'department', 'priority', 'title', 'description', 'assigned_to', 'assigned_to_ids',
            'created_by', 'status', 'due_date', 'start_date', 'completion_date'
        ]

    def get_assigned_to(self, obj):
        """Get the assigned employees for the task."""
        task_employees = TaskEmployeeModel.objects.filter(task=obj)
        return TaskEmployeeSerializer(task_employees, many=True).data

    def create(self, validated_data):
        """
        Create a new Task instance.

        This method handles the creation of a Task instance and assigns it to multiple Employees.
        """
        assigned_to_ids = validated_data.pop('assigned_to_ids')
        task = Task.objects.create(**validated_data)
        for employee in assigned_to_ids:
            TaskEmployeeModel.objects.create(task=task, employee=employee)
        return task

    def update(self, instance, validated_data):
        """
        Update an existing Task instance.

        This method handles the update of a Task instance and reassigns it to multiple Employees if needed.
        """
        assigned_to_ids = validated_data.pop('assigned_to_ids', None)
        if assigned_to_ids is not None:
            TaskEmployeeModel.objects.filter(task=instance).delete()
            for employee in assigned_to_ids:
                TaskEmployeeModel.objects.create(task=instance, employee=employee)
        return super().update(instance, validated_data)
