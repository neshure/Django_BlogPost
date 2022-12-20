from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  #Model form interacts with
  class Meta:
    model = User
  #Fields that's going to be shown
    fields = ['username', 'email', 'password1', 'password2']