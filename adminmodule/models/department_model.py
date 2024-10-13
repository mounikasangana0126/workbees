from django.db import models
from adminmodule.models.user_model import User

class ParentModel(models.Model):
    parent_dept = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.parent_dept

class DepartmentModel(models.Model):
    dept_name = models.CharField(max_length=255,unique=True)
    dept_code= models.CharField(max_length=255,unique=True)
    reporting_head=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    parent = models.ForeignKey(ParentModel,on_delete=models.SET_NULL,null=True)
    dept_is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.dept_name
    