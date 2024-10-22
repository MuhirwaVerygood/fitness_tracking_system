from django import forms
from .models import DailyActivity

class DailActivityForm(forms.ModelForm):
    class Meta:
        model = DailyActivity
        fields = '__all__'
        # to list fields to exclude from viewing them on a form
        # use below technique
        # exclude = ['registration_date', 'status'] 