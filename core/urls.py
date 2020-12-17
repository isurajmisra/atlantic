from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_view, name='home'),
    # path('admin/', views.admin_view, name='admin_view'),
    path('gallery/', views.gallery_view, name='gallery_view'),
    path('category/<int:cat_id>/subcat/<int:sub_id>/', views.sub_category_view, name='sub_category_view'),
    # path('login/', views.login, name='login'),
    # path('account_settings/', views.account_settings, name='account_settings'),
    ]