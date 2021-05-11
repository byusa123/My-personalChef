from django.db import models
from account.models import *
from personalChef import settings


# Create your models here.

CATEGORY = [
    ('Lunch', 'Lunch'),
    ('BreakFast', 'BreakFast'),
    ('Dinner', 'Dinner'),
]

# MEAL CLASS


class Meal(models.Model):
    name = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=40, choices=CATEGORY, default='Dinner')
    
    def __str__(self):
        return self.name




