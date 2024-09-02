from django.db import models
from adminmodule.models.user_model import User
from django.utils import timezone

class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True) 
    is_completed = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.user.username} - {self.clock_in} to {self.clock_out}"

    def total_work_time(self):
        if not self.clock_out:
            return None
        
        work_duration = (self.clock_out - self.clock_in).total_seconds()
        breaks_duration = sum([break_entry.duration_in_seconds() for break_entry in self.breakentry_set.all()])
        total_work_seconds = work_duration - breaks_duration
        
        return total_work_seconds / 3600 

