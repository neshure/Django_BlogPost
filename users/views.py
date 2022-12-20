from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


#Create a page for Users profile

@login_required #adds functionality to profile view. User must be logged in to view page
def profile(request):
    return render(request, 'users/profile.html')

''' 
  Types of flash messages: 
  messages.success
  messages.warning
  messages.info
  messages.error
  messages.debug
  
'''
