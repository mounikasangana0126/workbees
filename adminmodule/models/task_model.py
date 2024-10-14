from django.db import models
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.user_model import User
from adminmodule.models.department_model import DepartmentModel
from utils.helper.timestamp_model import TimeStampedModel

class Task(TimeStampedModel):
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    PRIORITY_CHOICES = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='LOW')
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')
    due_date = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return f"Task from {self.start_time} to {self.end_time}"
