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
from PIL import Image
from django.contrib.auth import login as user_login
from django.contrib import messages
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import  *

def home_view(request):

    # img = Image.open(r"C:\Users\suraj\Documents\atlantic\atlantic\core\static\img\img1.jpg")
    # im_desktop = img.resize((2000,500))
    # im_tablet = img.resize((800, 500))
    # im_mobile = img.resize((600, 500))
    # im_desktop.save("core\static\img\im_desktop.jpg")
    # im_tablet.save("core\static\img\im_tablet.jpg")
    # im_mobile.save("core\static\img\im_mobile.jpg")
    banners = ModifiedImg.objects.all()
    b = banners.last()
    print(b.banner_desktop.name)
    context = {'banners':banners}
    # if user.is_authenticated:
    #     if user.user_type == 'student':
    #         return render(request, 'home.html')
    #     elif user.user_type == 'teacher':
    #         return redirect('my_jobs')
    return render(request, 'home.html', context=context)

def gallery_view(request):
    return render(request, 'gallery.html')

def admin_view(request):
    return render(request, 'admin.html')

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
