from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm


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
            'is_chef'
        ]
# class userForm(ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         exclude = ['username']


class UpdateChefForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


