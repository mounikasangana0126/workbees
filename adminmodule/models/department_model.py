"""Department model."""

from django.db import models
from django.utils import timezone
from utils.helper.timestamp_model import TimeStampedModel 

class ParentModel(TimeStampedModel):
    """Parent model."""

    parent_dept = models.CharField(max_length=255,unique=True)
    def __str__(self):
        """Ruturn the string response of object."""
        return self.parent_dept

class DepartmentModel(TimeStampedModel):
    """Department model."""
    
    dept_name = models.CharField(max_length=255,unique=True)
    dept_code= models.CharField(max_length=255,unique=True)
    parent = models.ForeignKey(ParentModel,on_delete=models.SET_NULL,null=True)
    dept_is_enabled = models.BooleanField(default=True)

    def __str__(self):
        """Return the string response of object."""
        return self.dept_name
    
