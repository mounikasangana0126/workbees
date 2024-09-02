from django.db import models
from adminmodule.models.department_model import DepartmentModel

class DesignationModel(models.Model):
    department= models.ForeignKey(DepartmentModel,on_delete=models.SET_NULL,null=True)
    designation_name = models.CharField(max_length=255,unique=True)
    designation_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.designation_name