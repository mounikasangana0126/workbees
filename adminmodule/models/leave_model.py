from django.db import models
from adminmodule.models.employee_model import Employees

class Leave(models.Model):
    LEAVE_TYPE_CHOICES = (
        ('SICK', 'Sick Leave'),
        ('VACATION', 'Vacation'),
        ('CASUAL', 'Casual Leave'),
        ('MATERNITY', 'Maternity Leave'),
        ('PATERNITY', 'Paternity Leave'),
        ('OTHER', 'Other Leave'),
    )

    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='leave_records')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(blank=True, null=True)  # Optional reason for leave
    status = models.CharField(
        max_length=10,
        choices=(
            ('PENDING', 'Pending'),
            ('APPROVED', 'Approved'),
            ('REJECTED', 'Rejected')
        ),
        default='PENDING'
    )
    applied_on = models.DateTimeField(auto_now_add=True)  # Timestamp when leave is applied
    approved_on = models.DateTimeField(null=True, blank=True)  # When leave is approved, if applicable

    def total_days(self):
        """Returns the total number of leave days."""
        return (self.end_date - self.start_date).days + 1  # +1 to include the start_date

    def __str__(self):
        return f"{self.employee.user.username} - {self.leave_type} from {self.start_date} to {self.end_date}"

    class Meta:
        verbose_name = 'Leave'
        verbose_name_plural = 'Leaves'
        ordering = ['-start_date']
