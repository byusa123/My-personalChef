from django.db import models
# from django.db.models.deletion import CASCADE
from django.db.models.lookups import IsNull
from account.models import *
from personalChef import settings


# Create your models here.

CATEGORY = [
    ('Lunch', 'Lunch'),
    ('BreakFast', 'BreakFast'),
    ('Dinner', 'Dinner'),
]

STATUS = [
    ('available', 'available'),
    ('taken', 'taken'),
]

APPOINTMENT = [
    ('waiting', 'waiting'),
    ('booked', 'booked'),
    ('active', 'active'),
    
]

# MEAL CLASS


class Meal(models.Model):
    user_chef  = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=30,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=40, choices=CATEGORY, default='Dinner')
    
    def __str__(self):
        return self.name





class Schedule(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS, default='available')
    user_chef = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_chef


class booking(models.Model):
    user_client = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=40, on_delete=models.CASCADE)
    appointment = models.CharField(max_length=40, choices=APPOINTMENT, default='active' )
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    numbers_people = models.IntegerField(null=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.status






