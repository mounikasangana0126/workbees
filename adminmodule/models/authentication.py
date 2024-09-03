from django.db import models

class AuthenticationModel(models.Model):
    email=models.EmailField(max_length=255, unique=True)
    password=models.CharField(max_length=255,unique=True)


    def __str__ (self):
        return f"{{self.email}},{{self.password}}"
