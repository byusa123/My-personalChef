from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.core.exceptions import ValidationError

# Create your models here.
SPECIALITY = (
    ('African Cuisine', 'African Cuisine'),
    ('Italian Cuisine', 'Italian Cuisine'),
    ('Indian Cuisine', 'Indian Cuisine'),
    ('none', 'none')

)


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='images/', default='defaulty.png')
    phone_number = models.CharField(unique=True, max_length=40)
    is_chef = models.BooleanField(default=False)
    speciality = models.CharField(max_length=30, choices=SPECIALITY, default='none', blank=True)
    rate = models.CharField(max_length=30, blank=True, verbose_name='Price/hr')

    def __str__(self):
        return self.username


STATUS = (
    ('Pending', 'Pending'),
    ('Active', 'Active'),
    ('Denied', 'Denied')
)


class Application(models.Model):
    GENDER = [('MALE', 'MALE'),
              ('FEMALE', 'FEMALE')
              ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER)
    app_letter = models.ImageField(upload_to='letter_files', default='next.png', blank=True)
    status = models.CharField(max_length=30, choices=STATUS, default='Pending', blank=True)

    def __str__(self):
        return self.email
