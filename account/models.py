from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.


class User(AbstractUser):
    profic_pic = models.ImageField(null=True, blank=True)
    phone_number = models.CharField(unique=True)
    

    def __str__(self):
        return self.username