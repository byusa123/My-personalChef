from django.shortcuts import render, redirect
# from .models importUser, 
# Create your views here.

def homePage(request):
    # users = A.objects.all()
    # context = {'users': users}
    return render(request, 'index.html')