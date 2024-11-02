"""Task model."""

from django.db import models
from adminmodule.models.time_entry_model import TimeEntry
from adminmodule.models.employee_model import Employees
from adminmodule.models.department_model import DepartmentModel
from utils.helper.timestamp_model import TimeStampedModel

class Task(TimeStampedModel):
    """Model to represent a task within a department, assigned to employees."""

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
    assigned_to = models.ManyToManyField(Employees, related_name='tasks')
    created_by = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='created_tasks')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')
    due_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} (Priority: {self.priority}, Status: {self.status})"
class TaskEmployeeModel(TimeStampedModel):
    
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees, on_delete= models.CASCADE)
    status = models.CharField(max_length= 50 , choices=STATUS_CHOICES, default='PENDING')
    
    def __str__(self):
        return self.task.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if all(assignment.status == 'COMPLETED' for assignment in self.task.taskemployeemodel_set.all()):
            self.task.status = 'COMPLETED'
        else:
            self.task.status = 'IN_PROGRESS'
        self.task.save()