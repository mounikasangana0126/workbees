from django.db import models
from django.utils import timezone
from utils.helper.timestamp_model import TimeStampedModel 

class ParentModel(TimeStampedModel):
    parent_dept = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.parent_dept

class DepartmentModel(TimeStampedModel):
    dept_name = models.CharField(max_length=255,unique=True)
    dept_code= models.CharField(max_length=255,unique=True)
    parent = models.ForeignKey(ParentModel,on_delete=models.SET_NULL,null=True)
    dept_is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.dept_name
    
