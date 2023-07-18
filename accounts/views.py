from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
                                authenticate, 
                                login as djangoLogin,
                                logout as djangoLogout
                                ) 
import os
from accounts.models import Profile, Ip
from home.models import Story

# User = get_user_model()
# Create your views here.

class MyPasswordResetView(PasswordResetView):
    template_name = 'accounts/forget_password.html'
    success_url = reverse_lazy('login')

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/reset_password.html'
    success_url = reverse_lazy('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user:
            djangoLogin(request, user)
            instance = Ip.objects.create(ip = request.META.get('REMOTE_ADDR'))
            instance.users.add(user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,'Username or Password incorrect')


    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm-password')
        
        User.objects.create_user(username = username, first_name = fname, last_name = lname, password=password)
        return redirect(reverse_lazy('login'))
    return render(request, 'accounts/register.html')

# def forget_password(request):
#     return render(request, 'accounts/forget_password.html')

@login_required
def profile(request):
    stories = Story.objects.filter(user__id = request.user.id)
    if request.method == 'POST':
        image = request.FILES.get('image')
        with open(os.path.join(settings.MEDIA_ROOT, 'profile', image.name), 'wb') as f:
            f.write(image.read())
            user = Profile.objects.get(user_id = request.user.id)
            user.image = os.path.join('profile', image.name)
            user.save()
    context = {
        'myStories':stories
    }
    return render(request=request, template_name='user-profile.html', context = context)

def logout(request):
    djangoLogout(request)
    return redirect('/accounts/login')

def change_password(request):
    if request.method == 'POST':
        userId = request.user.id
        print(userId)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.get(id = int(userId))
            user.set_password(password1)
            user.save()
        else:
            print('===> errror yarandi')
            messages.add_message(request, messages.WARNING, 'Wrong password')


    return render(request, 'accounts/change_password.html')