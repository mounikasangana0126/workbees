from rest_framework import serializers
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.user_model import User

class TimeEntrySerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model = TimeEntry
        fields = '__all__'