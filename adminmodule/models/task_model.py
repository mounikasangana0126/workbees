from django.db import models
from adminmodule.models.time_entry_model import TimeEntry

class Task(models.Model):
    time_entry = models.ForeignKey(TimeEntry, on_delete=models.CASCADE)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    

    def __str__(self):
        return f"Task from {self.start_time} to {self.end_time}"
