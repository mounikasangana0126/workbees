from adminmodule.models.break_entry_model import BreakEntry
from rest_framework import serializers
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees
from adminmodule.models.user_model import User
from adminmodule.models.designation_model import DesignationModel

class DesiganetionCheckInCheckOut(serializers.ModelSerializer):
    class Meta:
        model=DesignationModel
        fields=['designation_name']
class UserCheckInChecout(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['name']
class BreakEntryCheckInCheckOut(serializers.ModelSerializer):
    class Meta:
        model = BreakEntry
        fields = ['break_start','break_end']
class TimeEntryCheckInCheckOut(serializers.ModelSerializer):
    breaks = BreakEntryCheckInCheckOut(many =True)
    class Meta:
        model= TimeEntry
        fields=['id','clock_in','clock_out','is_completed','work_mode','date', 'breaks']
        
class EmployeeCheckInCheckOut(serializers.ModelSerializer):
    timeentry = TimeEntryCheckInCheckOut(many = True)
    user=UserCheckInChecout()
    designation=DesiganetionCheckInCheckOut()
    class Meta:
        model=Employees
        fields=['user','employee_id','profile_pic','designation', 'timeentry']
