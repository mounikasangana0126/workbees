from django.db import models

class myuser(models.Model):
    emial=models.EmailField(max_length=255,unique=True)
    password=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return f"{self.emial} {self.password}"
