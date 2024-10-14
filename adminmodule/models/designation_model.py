from django.db import models
from utils.helper.timestamp_model import TimeStampedModel

class DesignationModel(TimeStampedModel):
    designation_name = models.CharField(max_length=255,unique=True)
    designation_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.designation_name