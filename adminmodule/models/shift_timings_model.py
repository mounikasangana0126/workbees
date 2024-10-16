from django.db import models
from datetime import datetime,date
from utils.helper.timestamp_model import TimeStampedModel

class WorkShiftsModel(TimeStampedModel):
    shift_name = models.CharField(max_length=255)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()
    break_time = models.FloatField(default=0.0)
    work_time = models.FloatField(default=0.0,null=True,blank=True)

    def save(self, *args, **kwargs):
        total_time = datetime.combine(date.min, self.shift_end_time) - datetime.combine(date.min, self.shift_start_time)
        total_hours=total_time.total_seconds() / 3600
        self.work_time= total_hours-self.break_time
        super(WorkShiftsModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.shift_name} ({self.shift_start_time} - {self.shift_end_time})"
    
# class UserShiftTimingsModel(TimeStampedModel):
#     employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
#     shift = models.ForeignKey(WorkShiftsModel, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.employee} - {self.shift}"