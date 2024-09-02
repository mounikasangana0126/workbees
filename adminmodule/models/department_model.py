from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=255,unique=True)
    parent_dept = models.CharField(max_length=255,unique=True)
    dept_is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.dept_name