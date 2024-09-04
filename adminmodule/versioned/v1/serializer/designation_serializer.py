from rest_framework import serializers
from adminmodule.models.designation_model import DesignationModel
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignationModel
        fields = '__all__'