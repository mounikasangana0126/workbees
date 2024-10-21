from rest_framework import serializers
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.versioned.v1.serializer.breakentry_serializer import BreakEntrySerializer
class TimeEntrySerializer(serializers.ModelSerializer):
    breaks = BreakEntrySerializer(many = True, read_only = True)
    class Meta:
        model = TimeEntry
        fields = ['employee','id','clock_in','clock_out','date','work_mode','is_completed','total_work_time','breaks']




