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
        form = createUserForm(request.POST, request.FILES)
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
    return render(request, 'userManagement/delete-chef.html', context)


def all_users(request):
    form = User.objects.all()
    context = {'form': form}
    return render(request, 'userManagement/allUsers.html', context)


def update_users(request, pk):
    user = User.objects.get(id=pk)
    form = createUserForm(instance=user)
    if request.method == 'POST':
        form = createUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('al_users')
    context = {'form': form}
    return render(request, 'userManagement/update-user.html', context)


def delete_user(request, pk):
    form = User.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form.delete()
            return redirect('al_users')
    context = {'form': form}
    return render(request, 'userManagement/delete-chef.html', context)



def chefApplication(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/application.html', context)

def allApplication(request):
    form = Application.objects.filter(status='Pending')
    context = {'form': form}
    return render(request, 'userManagement/all-application.html', context)


# def approveApplication(request, pk):
#     form = Application.objects.get(id=pk).update(status='Active')
#     return redirect('applicants')

def approveApplication(request, pk):
    data = Application.objects.get(pk=pk)
    form = ApproveApplicationForm()
    if request.method == 'POST':
        form = ApproveApplicationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            Application.objects.filter(pk=pk).update(status='Active')
            messages.success(request, 'Application Approved Successfully!.')
            return redirect('applicants')
    context = {'form': form, 'data': data}
    return render(request, 'userManagement/approve.html', context)


def denyApplication(request, pk):
    data = Application.objects.get(pk=pk)
    form = ApproveApplicationForm()
    if request.method == 'POST':
        form = ApproveApplicationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            Application.objects.filter(pk=pk).update(status='Denied')
            messages.success(request, 'Application Approved Successfully!.')
            return redirect('applicants')
    context = {'form': form, 'data': data}
    return render(request, 'userManagement/reject.html', context)


def viewApplication(request, pk):
    form = Application.objects.get(id=pk)
    context = {'form': form}
    return render(request, 'userManagement/view-application.html', context)
