from django.urls import path 
from django.contrib import admin
from . import views 

urlpatterns = [
    path('index', views.index , name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]