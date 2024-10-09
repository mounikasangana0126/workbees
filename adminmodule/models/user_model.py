from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email= models.EmailField(unique=True,null=True,blank=True)
    username = models.CharField(max_length=255, unique=True,null=True,blank=True)
    phone_number= models.CharField(max_length=10,null=True,blank=True)
    is_admin = models.BooleanField(default=False)  
    created_at= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name