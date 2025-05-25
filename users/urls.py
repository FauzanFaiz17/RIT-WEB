from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.maintenance, name='login'),
    path('register/', views.register, name='register'),
    path('it-community/', views.maintenance, name='it-community'),
    path('game-community/', views.maintenance, name='game-community'),
    path('game-division/', views.maintenance, name='game-division'),
    path('web-division/', views.maintenance, name='web-division'),
    path('iot-division/', views.maintenance, name='iot-division'),
    path('activities/', views.maintenance, name='activities'),
]

