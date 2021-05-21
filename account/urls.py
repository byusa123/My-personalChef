from django.urls import path
from . import views

urlpatterns = [
    # path('', views.homePage, name='homePage'),
  
    path('dashboard2/', views.home, name='dashboard2'),
    # path('', views.homePage1, name='homePage1'),

    path('register/', views.registerUser, name='register'),
    path('signup/', views.signUp, name='signup'),

    path('all-chefs/', views.all_chef, name='all_chefs'),
    path('update-chefs/<str:pk>/', views.update_chef, name='update_chefs'),
    path('delete-chefs/<str:pk>/', views.delete_chef, name='delete_chefs'),

    path('al-users/', views.all_users, name='al_users'),


]