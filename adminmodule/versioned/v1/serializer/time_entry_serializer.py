from rest_framework import serializers
from adminmodule.models.time_entry_model import TimeEntry

class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = '__all__'