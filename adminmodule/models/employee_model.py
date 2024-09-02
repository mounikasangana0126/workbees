from django.db import models
from adminmodule.models.user_model import User
from adminmodule.models.department_model import DepartmentModel
from adminmodule.models.designation_model import DesignationModel
from adminmodule.models.shift_timings_model import WorkShiftsModel

class Employees(models.Model):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    department = models.ForeignKey(
        DepartmentModel, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='employees'
    )
    designation =models.ForeignKey(
        DesignationModel, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='employees'
    )
    employee_id = models.CharField(max_length=50, unique=True)
    emp_is_active = models.BooleanField(default=True)
    auto_clockout = models.CharField(max_length=10, choices=STATUS_CHOICES, default='INACTIVE')
    location = models.CharField(max_length=255, blank=True, null=True)
    immediate_superior = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='immediate_subordinates')
    functional_superior = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='functional_subordinates')
    hr_superior = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='hr_subordinates')
    is_immediate = models.BooleanField(default=False)
    is_functional = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def is_hr(self):
        return self.roles.filter(name='HR').exists()

    def is_functional_manager(self):
        return self.roles.filter(name='Functional Manager').exists()

    def is_immediate_manager(self):
        return self.roles.filter(name='Immediate Manager').exists()

    