from rest_framework import serializers
from adminmodule.models.user_model import User
from adminmodule.models.employee_model import Employees
class UserSerializer(serializers.ModelSerializer):
    profile_pic = serializers.SerializerMethodField(read_only=True)
    employee_id = serializers.CharField(source='employee.employee_id', default=None,read_only=True)
    designation = serializers.CharField(source='employee.designation.designation_name', default=None,read_only=True)

    class Meta:
        model = User
        fields = ['id','name', 'username', 'email', 'profile_pic', 'employee_id', 'designation']

    def get_profile_pic(self, obj):
        """Retrieve profile picture URL if available."""
        employee=Employees.objects.get(user=obj)
        if employee and employee.profile_pic:
            profile_pic=Employees.objects.get(user=obj).profile_pic.url
        else:
            profile_pic=None
        return profile_pic
