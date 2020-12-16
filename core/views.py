import datetime
import json
import os
import re
import secrets
from django.db.models import Q
# from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render, redirect
import sqlite3

from django.contrib.auth import login as user_login
from django.contrib import messages
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

def home_view(request):
    user = request.user
    if user.is_authenticated:
        if user.user_type == 'student':
            return render(request, 'home.html')
        elif user.user_type == 'teacher':
            return redirect('my_jobs')
    return render(request, 'home.html')

def gallery_view(request):
    return render(request, 'gallery.html')

# def register(request):
#     if request.user.is_anonymous:
#         return render(request, 'register.html')
#     else:
#         return redirect("my_requests")
#
# def login(request):
#     if request.user.is_anonymous:
#         if request.method == "POST":
#             user = User.objects.filter(email=request.POST.get('email', ''))
#             if user.exists():
#                 if user.first().check_password(request.POST.get('password', '')):
#                     user_login(request, user.first())
#                     user = user.first()
#                     messages.success(request, "Login successful!!")
#                     if user.user_type == 'student':
#                         return redirect('my_requests')
#                     elif user.user_type == 'teacher':
#                         return redirect("account_settings")
#                 else:
#                     messages.error(request, "Credentials not valid!")
#                     return redirect('login')
#             else:
#                 messages.error(request, "Email is not registered!")
#                 return redirect('register')
#             return redirect('home')
#         return render(request, 'login.html')
#     else:
#         return redirect("my_requests")
