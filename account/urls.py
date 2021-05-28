from django.urls import path
from . import views

urlpatterns = [
    
  
    path('dashboard2/', views.home, name='dashboard2'),
 

    path('register/', views.registerUser, name='register'),
    path('signup/', views.signUp, name='signup'),

    path('all-chef-users/', views.all_chef_users, name='all_chef_users'),
    path('update-chefs/<str:pk>/', views.update_chef, name='update_chefs'),
    path('delete-chefs/<str:pk>/', views.delete_chef, name='delete_chefs'),

    path('al-users/', views.all_users, name='al_users'),
    path('update-user/<str:pk>/', views.update_users, name='update_user'),
    path('delete-user/<str:pk>/', views.delete_user, name='delete_user'),


    path('apply/', views.chefApplication, name='apply'),
    path('all-applicants/', views.allApplication, name='applicants'),
    path('view-applicant/<int:pk>/', views.viewApplication, name='view_applicants'),
    path('approve-applicant/<int:pk>/', views.approveApplication, name='approve_applicants'),
    path('deny-applicant/<int:pk>/', views.denyApplication, name='deny_applicants'),

    path('users', views.DashboardView.as_view(), name='users'),


]