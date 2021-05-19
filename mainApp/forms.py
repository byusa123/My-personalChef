from django.forms import ModelForm, fields
from .models import *


class CreateMealsForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        # user_chef = User.objects.filter(is_chef=True)
        super(CreateMealsForm, self).__init__(*args, **kwargs)
        self.fields['user_chef'].queryset = User.objects.filter(username=self.request.user.username)
        self.fields['user_chef'].empty_label = None
