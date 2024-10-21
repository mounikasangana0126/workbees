"""Department head model."""

from django.db import models
from adminmodule.models.employee_model import Employees
from utils.helper.timestamp_model import TimeStampedModel
from adminmodule.models.department_model import DepartmentModel

class DepartmentHeadModel(TimeStampedModel):
    """Department head model."""

    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    reporting_head = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        """Returns string response of the object."""
        return self.department.dept_name