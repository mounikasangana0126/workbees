from django.db import models
from adminmodule.models.employee_model import Employees
from django.utils import timezone
from utils.helper.timestamp_model import TimeStampedModel

class TimeEntry(TimeStampedModel):
    work_mode_choices = [
        ('WFO', 'Work From Office'),
        ('WFH', 'Work From Home'),
    ]
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    date= models.DateField(default=timezone.now)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True) 
    work_mode=models.CharField(choices=work_mode_choices,null=True,blank=True,max_length=50,default='WFH')
    is_completed = models.BooleanField(default=False) 

    def save(self, *args, **kwargs):
        if self.employee.employee_shift and self.employee.employee_shift.work_time:
            work_time_hours= self.employee.employee_shift.work_time
        else: 
            work_time_hours=9
        if self.clock_in and not self.clock_out:
            clock_out_hours = work_time_hours
            self.clock_out= self.clock_in + timezone.timedelta(hours=clock_out_hours)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.user.username} - {self.clock_in} to {self.clock_out}"

    def total_work_time(self):
        if not self.clock_out:
            return None
        
        work_duration = (self.clock_out - self.clock_in).total_seconds()
        breaks_duration = sum([break_entry.duration_in_seconds() for break_entry in self.breakentry_set.all()])
        total_work_seconds = work_duration - breaks_duration
        
        return total_work_seconds / 3600 

    def remaining_hours_after_clock_out(self):
        """ Calculate remaining hours based on expected duration. """
        if self.clock_out:
            expected_duration = self.employee.employee_shift.work_time  
            actual_duration = self.total_work_time() or 0  
            

            remaining_hours = expected_duration - actual_duration
            return max(remaining_hours, 0)  
        return None  

 