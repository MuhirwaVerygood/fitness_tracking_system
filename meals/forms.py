from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'
        # to list fields to exclude from viewing them on a form
        # use below technique
        # exclude = ['registration_date', 'status'] 