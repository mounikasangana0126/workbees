from django.db import models
from adminmodule.models.user_model import User
from django.utils import timezone
from adminmodule.models.time_entry_model import TimeEntry
from utils.helper.timestamp_model import TimeStampedModel


class BreakEntry(TimeStampedModel):
    """Breakentry model"""
    
    time_entry = models.ForeignKey(TimeEntry, on_delete=models.CASCADE, related_name='breaks')
    break_start = models.DateTimeField()
    break_end = models.DateTimeField(null=True, blank=True) 

    def save(self, *args, **kwargs):
        if self.break_start and self.break_end:
            break_duration = (self.break_end - self.break_start).total_seconds()
            if self.time_entry.clock_out: 
                self.time_entry.clock_out += timezone.timedelta(seconds=break_duration)
            else:
                self.time_entry.clock_out = self.break_end
            self.time_entry.save()
        super().save(*args, **kwargs)

    def __str__(self):
        """ return string in response of the object."""
        return f"Break - {self.break_start} to {self.break_end}"

    def duration_in_seconds(self):
        """ break time duration."""
        if not self.break_end:
            return 0
        return (self.break_end - self.break_start).total_seconds()
