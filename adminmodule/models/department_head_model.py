from django.db import models
from adminmodule.models.employee_model import Employees
from utils.helper.timestamp_model import TimeStampedModel
from adminmodule.models.department_model import DepartmentModel

class DepartmentHeadModel(TimeStampedModel):
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    reporting_head = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return self.department.dept_name