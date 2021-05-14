from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Meal, Schedule, booking
from .serializer import MealSerializer, ScheduleSerializer, bookingSerializer
from rest_framework import status

# Create your views here.

def index(request):
    return render(request, 'index.html')

class MealList(APIView):
    def get(self, request, format=None):
        all_meal = Meal.objects.all()
        serializers = MealSerializer(all_meal, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MealSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    

class ScheduleList(APIView):
    def get(self, request, format=None):
        all_schedule = Schedule.objects.all()
        serializers = ScheduleSerializer(all_schedule, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = ScheduleSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

class bookingList(APIView):
    def get(self, request, format=None):
        all_booking = booking.objects.all()
        serializers = bookingSerializer(all_booking, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = bookingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)