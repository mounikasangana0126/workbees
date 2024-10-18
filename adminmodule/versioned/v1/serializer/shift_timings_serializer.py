from rest_framework import serializers
from adminmodule.models.shift_timings_model import WorkShiftsModel
class ShiftTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkShiftsModel
        fields=['id','shift_name','shift_start_time','shift_end_time','break_time','work_time']