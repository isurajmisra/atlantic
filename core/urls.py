from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_view, name='home'),
    # path('admin/', views.admin_view, name='admin_view'),
    path('gallery/', views.gallery_view, name='gallery_view'),
    path('category/<int:cat_id>/', views.category_view, name='category_view'),
    path('category/<int:cat_id>/subcat/<int:sub_id>/', views.sub_category_view, name='sub_category_view'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('term_and_conditions/', views.term_conditions_view, name='term_conditions_view'),
    path('help_center/', views.help_center_view, name='help_center_view'),
    path('support_policy/', views.support_policy_view, name='support_policy_view'),
    ]