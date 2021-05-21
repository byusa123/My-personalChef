from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework import status
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView
from .forms import *

# Create your views here.



'''
Start of chefdashboard functions
'''
def addMeals(request):
    form = CreateMealsForm(request=request)

    if request.method == 'POST':
        form = CreateMealsForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('add_meals')

    context = {'form': form}
    return render(request, 'chefDashboard/addmeals.html', context)
'''
End of chefdashboard functions
'''

def index(request):
    chefs = User.objects.filter(is_chef=True)
    meals_lunch = Meal.objects.filter(category='Lunch')
    meals_break = Meal.objects.filter(category='BreakFast')
    meals_dinner = Meal.objects.filter(category='Dinner')
    context = {'chefs': chefs, 'meals_lunch': meals_lunch, 'meals_break': meals_break, 'meals_dinner': meals_dinner}
    return render(request, 'index.html', context)


def chef_detail(request, id):
    chef = User.objects.get(pk=id)
    # chef = User.objects.filter(pk=self.kwargs['user_id']).first()
    schedules = Schedule.get_schedule_by_chef(id)
    return render(request, 'chef_detail.html', {"chef": chef, "schedules": schedules})

# def book(request,schedule_id):

#     if request.method=='POST':


#     else:
#         form = BookingForm()
#         return render(request, 'booking.html', {"form":form, "schedule_id":schedule_id})

def book(request,schedule_id):

    if request.method=='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            numberOfPeople = form.cleaned_data['numberOfPeople']
            location = form.cleaned_data['location']
            schedule = Schedule.objects.get(pk=schedule_id)
            new_booking = Booking(first_name = first_name, last_name = last_name,  email = email, phone_number=phone_number, numberOfPeople=numberOfPeople, location=location, schedule = schedule )
            new_booking.save()
            Schedule.taken_schedule(schedule_id)
            # scontextend_welcome_email(first_name,last_name,schedule,email)
            return render(request, 'booking-success.html', {"booking":new_booking})
    else:
        form = BookingForm()
        return render(request, 'booking.html', {"form":form, "schedule_id":schedule_id})
'''
API PART START
'''

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
        all_booking = Booking.objects.all()
        serializers = BookingSerializer(all_booking, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BookingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


'''
API PART END
'''
