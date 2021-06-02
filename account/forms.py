from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm
from django import forms


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'profile_pic',
            'is_chef',
            'speciality',
            'rate'
        ]


class UpdateChefForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class UpdateProfile(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['rate']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['status']


class ApproveApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('status',)
