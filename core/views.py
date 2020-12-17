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
    banners = ModifiedImg.objects.all()
    logo_fav = LogoFav.objects.all().first()
    categories = ServiceCategory.objects.all()

    context = {'banners':banners, 'logo_fav':logo_fav, 'categories':categories}

    return render(request, 'home.html', context=context)

def gallery_view(request):
    gallery = Gallery.objects.all()
    logo_fav = LogoFav.objects.all().first()
    categories = ServiceCategory.objects.all()
    context = {'gallery':gallery, 'logo_fav':logo_fav, 'categories':categories}
    return render(request, 'gallery.html', context=context)

# def admin_view(request):
#     return render(request, 'admin.html')

def sub_category_view(request, cat_id, sub_id):
    logo_fav = LogoFav.objects.all().first()
    categories = ServiceCategory.objects.all()
    category = ServiceCategory.objects.filter(id=cat_id).first()
    sub = ServiceSubCategory.objects.filter(id=sub_id).first()
    return render(request, 'subCategory.html', {'category': category, 'subcategory': sub, 'logo_fav':logo_fav, 'categories':categories})

def contact_view(request):
    logo_fav = LogoFav.objects.all().first()
    categories = ServiceCategory.objects.all()
    context = {'logo_fav': logo_fav, 'categories': categories}
    return render(request, 'contact.html', context=context)

def about_view(request):
    logo_fav = LogoFav.objects.all().first()
    categories = ServiceCategory.objects.all()
    context = {'logo_fav': logo_fav, 'categories': categories}
    return render(request, 'about.html', context=context)

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
