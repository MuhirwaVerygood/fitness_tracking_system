from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = '__all__'
        # to list fields to exclude from viewing them on a form
        # use below technique
        # exclude = ['registration_date', 'status'] 