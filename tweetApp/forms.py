from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    class Meta: # Meta is used to configure the ModelForm (model + fields).
        model = Tweet   # Link this form to the Tweet model
        fields = ['text', 'photo']   # Fields to show in the form

class UserRegistrationForm(UserCreationForm):   # Built-in Django form for user registration
    email = forms.EmailField()  # Adding an email field explicitly to the registration form
    class Meta:
        model = User # Django’s default User model 
        fields = ('username', 'email', 'password1', 'password2') 
        # Tuple of fields to include in the form (password1 & password2 are provided by UserCreationForm for confirmation)
