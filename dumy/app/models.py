from django.db import models

# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    dob=models.CharField(max_length=40)