from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def homePage(request):
    # users = A.objects.all()
    # context = {'users': users}
    return render(request, 'admin/base.html')


def homePage1(request):
    # users = A.objects.all()
    # context = {'users': users}
    return render(request, 'index.html')



def registerPage(request):
    context = {}
    return render()