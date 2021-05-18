from django.forms import ModelForm, fields
from .models import *


class CreateMealsForm(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # user_chef = User.objects.filter(is_chef=True)
        super(CreateMealsForm, self).__init__(*args, **kwargs)
        self.fields['user_chef'].queryset = User.objects.filter(is_chef=True)
        self.fields['user_chef'].empty_label = None
