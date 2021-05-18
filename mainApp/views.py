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
Function written by INGABIRE PART
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


def index(request):
    chefs = User.objects.filter(is_chef=True)
    meals_lunch = Meal.objects.filter(category='Lunch')
    meals_break = Meal.objects.filter(category='BreakFast')
    meals_dinner = Meal.objects.filter(category='Dinner')
    context = {'chefs': chefs, 'meals_lunch': meals_lunch, 'meals_break': meals_break, 'meals_dinner': meals_dinner}
    return render(request, 'index.html', context)

'''
Function written by INGABIRE END
'''


# def index(request):
#     user_chef = User.objects.all()
#
#     meals = Meal.objects.all()
#     print(meals)
#
#     return render(request, 'index.html', {"user_chef": user_chef, "meals": meals})
#

# class indexView(ListView):
#     template_name = 'index.html'
#     model = Meal

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context=super(indexView, self).get_context_data(**kwargs)
#         context['all_break'] = Meal.objects.filter(category ='Breakfast')
#         return context


def chef_detail(request, id):
    single_chef = User.objects.get(pk=id)
    schedules = Schedule.get_schedule_by_chef(id)
    return render(request, 'chef_detail.html', {"single_chef": single_chef, "schedules": schedules})


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
