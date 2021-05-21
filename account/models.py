from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='images/' , default='defaulty.png') 
    phone_number = models.CharField(unique=True, max_length=40)
    is_chef = models.BooleanField(default=False)

    def __str__(self):
        return self.username
