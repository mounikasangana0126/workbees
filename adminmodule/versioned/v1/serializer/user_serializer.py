from rest_framework import serializers
from adminmodule.models.user_model import User
from adminmodule.versioned.v1.serializer.time_entry_serializer import TimeEntrySerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
