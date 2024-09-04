from rest_framework import serializers
from adminmodule.models.time_entry_model import TimeEntry
class ShiftTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TimeEntry
        fields='__all__'