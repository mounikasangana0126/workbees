from django.db import models

class DesignationModel(models.Model):
    designation_name = models.CharField(max_length=255,unique=True)
    designation_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.designation_name