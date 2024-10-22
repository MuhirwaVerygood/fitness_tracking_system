# forms.py
from django import forms
from .models import User  

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'date_of_birth', 'gender', 'weight', 'height']
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Set date input for date_of_birth
        }


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 4:  # Example validation
            raise forms.ValidationError("Password must be at least 4 characters long.")
        return password
