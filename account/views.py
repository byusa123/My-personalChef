from personalChef.settings import EMAIL_HOST_USER
from mainApp import email
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from .models import User
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import smtplib
from email.message import EmailMessage
from django.views.generic import ListView, CreateView, DetailView, UpdateView


# Create your views here.

def homePage(request):
    # users = A.objects.all()
    # context = {'users': users}
    return render(request, 'firstPage.html')


@login_required
def home(request):
    return render(request, 'baseAdmin/base.html')


@login_required()
def registerUser(request):
    try:

        form = createUserForm()
        if request.method == 'POST':
            form = createUserForm(request.POST or None, request.FILES)
            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                email = form.cleaned_data.get('email')
                fn = form.cleaned_data.get('first_name')
                my_mail = EmailMessage()
                my_mail['from'] = "MyChef"
                my_mail["to"] = email
                my_mail['subject'] = "MyChef Login Credentials"
                email_content = f'Dear {fn.upper()}, Thank you, you have received this email because you have ' \
                                f'Applied to be a chef at MyChef  you can use the following username and password ' \
                                f'to login in to our website.  ' \
                                f'Username: {username}  Password: {password}. ' \
                                f'from MyChef'

                my_mail.set_content(email_content)
                with smtplib.SMTP(host="smtp.gmail.com", port=587) as help:
                    help.ehlo()
                    help.starttls()
                    help.login('wemychef@gmail.com', 'wecode2020')
                    help.send_message(my_mail)

                    form = createUserForm()
                messages.success(request, "User Created Successfully..")
    except ValueError:
        form = createUserForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def signUp(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            # username = form.cleaned_data.get('username')

    # messages.success(request, 'The chef was successful created'+username)

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def all_chef_users(request):
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
            return redirect('all_chef_users')
    context = {'form': form}
    return render(request, 'userManagement/update-chef.html', context)


def update_profile(request):
    user = User.objects.get(username=request.user.username)
    form = UpdateProfile(instance=user)
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    context = {'form': form}
    return render(request, 'chefDashboard/update-profile.html', context)


def user_profiling(request):
    data = User.objects.filter(username=request.user.username)
    context = {'data': data}
    return render(request, 'chefDashboard/profiling.html', context)


def delete_chef(request, pk):
    form = User.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form.delete()
            return redirect('all_chef_users')
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


def approveApplication(request, pk):
    try:
        data = Application.objects.get(pk=pk)
        form = ApproveApplicationForm(instance=data)
        if request.method == 'POST':
            form = ApproveApplicationForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                Application.objects.filter(pk=pk).update(status='Active')

                email = data.email
                fn = data.first_name
                my_mail = EmailMessage()
                my_mail['from'] = "MyChef"
                my_mail["to"] = email
                my_mail['subject'] = "MyChef Application Accepted"
                email_content = f'Dear {fn}, Thank you, you have received this email because you have ' \
                                f'Applied to be a chef at MyChef.Your application was accepted' \
                                f'you will soon receive your account credentials.  ' \
                                f'from MyChef'

                my_mail.set_content(email_content)
                with smtplib.SMTP(host="smtp.gmail.com", port=587) as help:
                    help.ehlo()
                    help.starttls()
                    help.login('wemychef@gmail.com', 'wecode2020')
                    help.send_message(my_mail)

                    form = ApproveApplicationForm()
                messages.success(request, "Application Approved Successfully..")
                return redirect('applicants')

    except ValueError:
        ApproveApplicationForm()

    context = {'form': form, 'data': data}
    return render(request, 'userManagement/approve.html', context)


def denyApplication(request, pk):
    try:
        data = Application.objects.get(pk=pk)
        form = ApproveApplicationForm(instance=data)
        if request.method == 'POST':
            form = ApproveApplicationForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                Application.objects.filter(pk=pk).update(status='Denied')

                email = data.email
                fn = data.first_name
                my_mail = EmailMessage()
                my_mail['from'] = "MyChef"
                my_mail["to"] = email
                my_mail['subject'] = "MyChef Application Denied"
                email_content = f'Dear {fn}, Thank you, you have received this email because you have ' \
                                f'Applied to be a chef at MyChef.Your application was denied ' \
                                f'Thank you for applying.  ' \
                                f'from MyChef'

                my_mail.set_content(email_content)
                with smtplib.SMTP(host="smtp.gmail.com", port=587) as help:
                    help.ehlo()
                    help.starttls()
                    help.login('wemychef@gmail.com', 'wecode2020')
                    help.send_message(my_mail)

                    form = ApproveApplicationForm()
                messages.success(request, "Application Denied ..")
                return redirect('applicants')

    except ValueError:
        ApproveApplicationForm()

    context = {'form': form, 'data': data}
    return render(request, 'userManagement/reject.html', context)


def viewApplication(request, pk):
    form = Application.objects.get(id=pk)
    context = {'form': form}
    return render(request, 'userManagement/view-application.html', context)


class DashboardView(ListView):
    model = User
    template_name = 'userManagement/dashboard.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all().count()
        return context
