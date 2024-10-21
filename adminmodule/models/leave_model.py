"""Leave Model"""

from django.db import models
from adminmodule.models.employee_model import Employees
from utils.helper.timestamp_model import TimeStampedModel
class Leave(TimeStampedModel):
    """Leave model"""
    LEAVE_TYPE_CHOICES = (
        ('SICK', 'Sick Leave'),
        ('VACATION', 'Vacation'),
        ('CASUAL', 'Casual Leave'),
        ('MARRIAGE', 'Marriage Leave'),
        ('UNPAID', 'Unpaid Leave'),
        ('OTHER', 'Other Leave'),
    )
    LEAVE_SHIFT_CHOICES=(
        ('FULL_DAY', 'Full Day'),
        ('FIRST_HALF', 'First Half'),
        ('SECOND_HALF', 'Second Half'),   
    )

    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='leave_records')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField() 
    status = models.CharField(
        max_length=10,
        choices=(
            ('PENDING', 'Pending'),
            ('APPROVED', 'Approved'),
            ('REJECTED', 'Rejected')
        ),
        default='PENDING'
    )
    leave_shift = models.CharField(max_length=20, choices=LEAVE_SHIFT_CHOICES, default='FULL_DAY')
    applied_on = models.DateTimeField(auto_now_add=True) 
    approved_on = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='approved_leaves', null=True, blank=True)  

    def total_days(self):
        """Returns the total number of leave days."""
        return (self.end_date - self.start_date).days + 1 

    def __str__(self):
        """Return String response of th object"""
        return f"{self.employee.user.username} - {self.leave_type} from {self.start_date} to {self.end_date}"

    class Meta:
        verbose_name = 'Leave'
        verbose_name_plural = 'Leaves'
        ordering = ['-start_date']
