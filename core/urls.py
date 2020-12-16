from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('gallery/', views.gallery_view, name='gallery_view'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('account_settings/', views.account_settings, name='account_settings'),
    ]