from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('connect/', views.connect, name='connect'),
    path('product/', views.product, name='product'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]