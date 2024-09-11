from django.db import models
class register(models.Model):
    email=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=10)
    repeatpassword=models.CharField(max_length=10)
    desig=models.CharField(max_length=15,default="user")
    name = models.CharField(max_length=50)  # Add this
    gender = models.CharField(max_length=10)
    


# Create your models here.
