from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxInput, ClearableFileInput, DateInput, ImageField, ModelForm, TextInput, EmailInput, Select, Textarea
from .models import *


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required, add a valid email')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')



class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields =['email', 'username', 'is_admin', 'is_active', 'is_staff', 'is_employee', 'is_hr']
