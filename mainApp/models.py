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
    ('notavailable', 'notavailable'),
]


# APPOINTMENT = [
#     ('waiting', 'waiting'),
#     ('booked', 'booked'),
#     ('active', 'active'),

# ]

# MEAL CLASS

class Meal(models.Model):
    user_chef = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=30, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    meal_image = models.ImageField(upload_to='meals', blank=True, default='food.png')
    description = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=40, choices=CATEGORY, default='Dinner')
    price = models.IntegerField(null=True, blank=True)

    def save_meal(self):
        self.save()

    def delete_meal(self):
        self.delete()

    def __str__(self):
        return self.name

    def all_meal(cls):
        return cls.objects.all()   


class Schedule(models.Model):
    day = models.CharField(max_length=30, blank=True)
    hour = models.CharField(max_length=30, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS, default='available')
    user_chef = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save_schedule(self):
        self.save()

    def delete_schedule(self):
        self.delete()

    @classmethod
    def get_schedule_by_chef(cls, user_id):
        return cls.objects.filter(user_chef=user_id, status='available').all()

    @classmethod
    def taken_schedule(cls, id):
        cls.objects.filter(id=id).update(status='notavailable')


class Booking(models.Model):
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    numberOfPeople = models.IntegerField(null=True)
    location = models.CharField(max_length=40, null=True, blank=True)

    def save_booking(self):
        self.save()
