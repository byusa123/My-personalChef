from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('home/', views.homePage1, name='homePage1'),
]