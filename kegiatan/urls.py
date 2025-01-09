from django.conf import settings
from django.urls import path
from . import views
from .views import register, user_login, user_logout, dashboard, icons, map, profile, tables, struktur

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('icons/', icons, name='icons'),
    path('map/', map, name='map'),
    path('profile/', profile, name='profile'),
    path('tables/', tables, name='tables'),
    path('struktur/', struktur, name='struktur'),
]