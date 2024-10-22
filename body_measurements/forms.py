from django import forms
from .models import BodyMeasurement

class BodyMeasurementForm(forms.ModelForm):
    class Meta:
        model = BodyMeasurement
        fields = '__all__'
        # to list fields to exclude from viewing them on a form
        # use below technique
        # exclude = ['registration_date', 'status'] 