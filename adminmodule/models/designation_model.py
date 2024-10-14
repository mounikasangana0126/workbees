from django.db import models
from utils.helper.timestamp_model import TimeStampedModel
from adminmodule.models.department_model import DepartmentModel

class DesignationModel(TimeStampedModel):
    department= models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    designation_name = models.CharField(max_length=255,unique=True)
    designation_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.designation_name