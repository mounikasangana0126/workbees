from adminmodule.versioned.v1.serializer.time_entry_serializer import TimeEntrySerializer
from adminmodule.versioned.v1.serializer.breakentry_serializer import BreakEntrySerializer
from rest_framework import serializers
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.user_model import User
from adminmodule.versioned.v1.serializer.designation_serializer import DesignationSerializer

        
class CheckinCheckoutSerializer(serializers.ModelSerializer):
    breakentry = BreakEntrySerializer(many=True,source='breaks', read_only=True)
    name=serializers.CharField(source='employee.user.name', default=None, read_only=True)

    class Meta:
        model=TimeEntry
        fields=['id','name','employee','date', 'clock_in','clock_out','is_completed','work_mode','breakentry']
