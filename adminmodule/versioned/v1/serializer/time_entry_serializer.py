from rest_framework import serializers
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.user_model import User
from adminmodule.versioned.v1.serializer.user_serializer import UserSerializer

class TimeEntrySerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = TimeEntry
        fields = ['user','clock_in','clock_out','is_completed','work_mode']