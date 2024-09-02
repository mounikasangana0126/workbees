from django.db import models
from user_model import User
from django.utils import timezone
from time_entry_model import TimeEntry

class BreakEntry(models.Model):
    time_entry = models.ForeignKey(TimeEntry, on_delete=models.CASCADE, related_name='breaks')
    break_start = models.DateTimeField()
    break_end = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return f"Break - {self.break_start} to {self.break_end}"

    def duration_in_seconds(self):
        if not self.break_end:
            return 0
        return (self.break_end - self.break_start).total_seconds()
