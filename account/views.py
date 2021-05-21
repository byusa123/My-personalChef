from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from .models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def homePage(request):
    # users = A.objects.all()
    # context = {'users': users}
    return render(request, 'firstPage.html')


# @method_decorator(login_required, name='dispatch')
def home(request):
    return render(request, 'baseAdmin/base.html')


def registerUser(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, 'The chef was successful created'+username)

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def signUp(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homePage1')
            # username = form.cleaned_data.get('username')
            # messages.success(request, 'The chef was successful created'+username)

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def all_chef(request):
    form = User.objects.filter(is_chef=True)
    context = {'form': form}
    return render(request, 'userManagement/all-chefs.html', context)


def update_chef(request, pk):
    user = User.objects.get(id=pk)
    form = createUserForm(instance=user)
    if request.method == 'POST':
        form = createUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all_chefs')
    context = {'form': form}
    return render(request, 'userManagement/update-chef.html', context)


def delete_chef(request, pk):
    form = User.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form.delete()
            return redirect('all_chefs')
    context = {'form': form}
    return render(request, 'userManagement/delete-user.html', context)


def all_users(request):
    form = User.objects.all()
    context = {'form': form}
    return render(request, 'userManagement/allUsers.html', context)
