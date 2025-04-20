from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import re

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required =True)

    class Meta:
        model  = User
        fields = ('username','email', 'password1', 'password2')

def clean_email(self):
    email = self.cleaned_data.get('email')
    try:
        EmailValidator()(email)
    except ValidationError:
        raise ValidationError("Please enter a valid emeil.")
    
    if User.objects.filter(email=email).exists():
        raise ValidationError("This email is already registered.")
    return email

def clean_password(self):
    password = self.cleaned_data.get('password1')

    if len(password<0):
        raise ValidationError("Password must be at least 8 characters long.")

    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
         raise ValidationError("Password must contain at least one lowercase letter.")

    if not re.search(r'[0-9]', password):
        raise ValidationError("Password must contain at least one number.")

    if not re.search(r'[@$!%*?&]', password):
        raise ValidationError("Password must contain at least one special character.")

    return password

def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

       
        if password1 != password2:
            raise ValidationError("Passwords do not match.")

        return password2