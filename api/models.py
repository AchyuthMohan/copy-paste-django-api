from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)

# Create your models here.
class Car(models.Model):
    car_name=models.CharField(max_length=20)
    car_price=models.FloatField()
    car_year=models.IntegerField()
    def __str__(self):
        return self.car_name