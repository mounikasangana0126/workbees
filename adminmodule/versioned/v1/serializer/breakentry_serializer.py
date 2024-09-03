from adminmodule.models.break_entry_model import BreakEntry
from rest_framework import serializers

class BreakEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakEntry
        fields = '__all__'
        
        