from django import forms
from .models import SleepLog

class SleepLogForm(forms.ModelForm):
    class Meta:
        model = SleepLog
        fields = '__all__'
        # to list fields to exclude from viewing them on a form
        # use below technique
        # exclude = ['registration_date', 'status'] 