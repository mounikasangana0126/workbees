from adminmodule.models.break_entry_model import BreakEntry
from rest_framework import serializers
from adminmodule.models.time_entry_model import TimeEntry

class BreakEntrySerializer(serializers.ModelSerializer):
    """Break entry serializer"""
    class Meta:
        model = BreakEntry
        fields = ['id','time_entry','break_start','break_end']
        
        