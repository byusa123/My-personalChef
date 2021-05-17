from django.urls import path
from . import views

urlpatterns = [
    # path('', views.homePage, name='homePage'),
  
    path('dashboard2/', views.home, name='dashboard2'),
    path('', views.homePage1, name='homePage1'),

    path('register/', views.registerUser, name='register'),
    path('signup/', views.signUp, name='signup'),
]