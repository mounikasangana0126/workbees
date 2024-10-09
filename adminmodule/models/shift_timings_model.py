from django.db import models
from adminmodule.models.user_model import User


class WorkShiftsModel(models.Model):
    shift_name = models.CharField(max_length=255)
    shift_start_time = models.TimeField()
    shift_end_time = models.TimeField()
    break_time= models.TimeField()  
    work_time = models.TimeField()  

    def save(self, *args, **kwargs):
        self.work_time = self.shift_end_time - self.shift_start_time - self.break_time
        super(WorkShiftsModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.label_name} ({self.start_time} - {self.end_time})"

    def get_total_working_hours(self):
        total_time = datetime.combine(date.min, self.end_time) - datetime.combine(date.min, self.start_time)
        total_hours = total_time.total_seconds() / 3600  
        break_hours = self.break_time / 60 
        return total_hours - break_hours

    
class UserShiftTimingsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shift = models.ForeignKey(WorkShiftsModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.shift}"