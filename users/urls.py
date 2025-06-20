from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.update_profile, name='profile'),
    path('update-foto-profil/', views.update_foto_profil, name='update_foto'),
    path('it-community/', views.maintenance, name='it-community'),
    path('game-community/', views.maintenance, name='game-community'),
    path('game-division/', views.maintenance, name='game-division'),
    path('web-division/', views.maintenance, name='web-division'),
    path('iot-division/', views.maintenance, name='iot-division'),
    path('activities/', views.maintenance, name='activities'),
]

