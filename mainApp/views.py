from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework import status
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView
from .forms import *
from .email import *
from django.contrib.auth.decorators import login_required

# Create your views here.


'''
Start of chefdashboard functions
'''


def addMeals(request):
    form = CreateMealsForm(request=request)

    if request.method == 'POST':
        form = CreateMealsForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return redirect('all_meals')

    context = {'form': form}
    return render(request, 'chefDashboard/addmeals.html', context)


def all_meals(request):
    form = Meal.objects.filter(user_chef_id=request.user.id)
    context = {'form': form}
    return render(request, 'chefDashboard/allmeals.html', context)


def update_meal(request, pk):
    meal = Meal.objects.get(id=pk)
    form = CreateMealsForm(instance=meal)
    if request.method == 'POST':
        form = CreateMealsForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('all_meals')
    context = {'form': form}
    return render(request, 'chefDashboard/update-meal.html', context)


def delete_meal(request, pk):
    form = Meal.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form.delete()
            return redirect('all_meals')
    context = {'form': form}
    return render(request, 'chefDashboard/delete-meal.html', context)


def addSchedule(request):
    form = ScheduleForm(request=request)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect('all_schedule')

    context = {'form': form}
    return render(request, 'chefDashboard/addSchedule.html', context)


def all_schedule(request):
    form = Schedule.objects.filter(user_chef_id=request.user.id)
    context = {'form': form}
    return render(request, 'chefDashboard/allSchedule.html', context)


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


def all_chef(request):
    chefs = User.objects.filter(is_chef=True)
    return render(request, 'all_chefs.html', context={"chefs": chefs})

def search_chef(request):
    if request.method == "GET":
        searched = request.GET['searched']
        chefs=User.objects.filter(first_name__contains=searched)
        return render(request, 'search_chef.html',context={"searched":searched, "chefs":chefs})
    else:
        return render(request, 'search_chef.html',{})

 




<<<<<<< HEAD
#     else:
#         form = BookingForm()
#         return render(request, 'booking.html', {"form":form, "schedule_id":schedule_id})
@login_required()
=======
def all_meals(request):
    meals= Meal.objects.all()
    return render(request, 'all_meals.html' , context={"meals": meals})

def meal_detail(request, id):
    meals = Meal.objects.get(pk=id)
    chef = User.objects.filter(pk=id)
    return render(request, 'meal_details.html', {"meals": meals, "chef": chef})

def search_meal(request):
    if request.method == "GET":
        searched = request.GET['searched']
        meals=Meal.objects.filter(name__contains=searched)
        return render(request, 'search_meal.html',context={"searched":searched, "meals":meals})
    else:
        return render(request, 'search_meal.html',{})



>>>>>>> 6903abbda4e338d5934160d6de8c6567e6673814
def book(request, schedule_id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            numberOfPeople = form.cleaned_data['numberOfPeople']
            location = form.cleaned_data['location']
            meals = form.cleaned_data['meals']
            add_info = form.cleaned_data['add_info']
            schedule = Schedule.objects.get(pk=schedule_id)
            new_booking = Booking(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                                  numberOfPeople=numberOfPeople, location=location, meals=meals, add_info=add_info, schedule=schedule)
            new_booking.save()
            Schedule.taken_schedule(schedule_id)

            # scontextend_welcome_email(first_name,last_name,schedule,email)
            confirmation_email(first_name, last_name, schedule, email)
            return render(request, 'booking-success.html', {"booking": new_booking})
    else:
        form = BookingForm()
        return render(request, 'booking.html', {"form": form, "schedule_id": schedule_id})


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
