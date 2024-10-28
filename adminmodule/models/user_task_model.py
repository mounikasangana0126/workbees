from utils.helper.timestamp_model import TimeStampedModel
from adminmodule.models.task_model import Task 
from adminmodule.models.employee_model import Employees
from django.db import models


class UserTaskModel(TimeStampedModel):
    """User task model."""
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    task = models.ForeignKey(Task,on_delete=models.CASCADE,null=True,blank=True)
    employee = models.ForeignKey(Employees,on_delete=models.CASCADE,null=True,blank=True)
    task_status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='PENDING')

    def __str__(self):
        """Return string response of the object."""
        return self.task.title
