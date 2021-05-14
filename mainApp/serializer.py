
from rest_framework import serializers
from .models import Meal, Schedule, booking

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ("id", "name", "user_chef", "date_created", "category")


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ("id", "date", "user_chef", "status")


class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ("id", "user_client", "user_chef", "status", "schedule", "number_people", "location" )
        