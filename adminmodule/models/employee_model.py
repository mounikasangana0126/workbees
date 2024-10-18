from django.db import models
from adminmodule.models.user_model import User
from adminmodule.models.designation_model import DesignationModel
from utils.helper.timestamp_model import TimeStampedModel
from adminmodule.models.shift_timings_model import WorkShiftsModel

class Employees(TimeStampedModel):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    designation =models.ForeignKey(
        DesignationModel, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='employee'
    )
    date_of_birth = models.DateField(null=True, blank=True)
    employee_id = models.CharField(max_length=50, unique=True)
    emp_is_active = models.BooleanField(default=True,null=True)
    employee_shift=models.ForeignKey(WorkShiftsModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='employee')
    auto_clockout = models.CharField(max_length=10, choices=STATUS_CHOICES, default='INACTIVE')
    city = models.CharField(max_length=255, blank=True, null=True)
    joining_date = models.DateField(null=True, blank=True)
    address=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.name


    