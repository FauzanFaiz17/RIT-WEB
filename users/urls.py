from django.urls import path
from .views import index,maintenance,game,register_user,login_view, dashboard, contoh,profile_view,update_foto_profil,Anggota,keuangan,inventaris,surat
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='home'),
    path('it-community/', maintenance, name='it-community'),
    path('game-community/', game, name='game-community'),
    path('game-division/', maintenance, name='game-division'),
    path('web-division/', maintenance, name='web-division'),
    path('iot-division/', maintenance, name='iot-division'),
    path('activities/', maintenance, name='activities'),


    path('register/', register_user, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('contoh/', contoh, name='contoh'),
    path('profile/', profile_view, name='profile'),
    path('update-foto/', update_foto_profil, name='update_foto'),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    
    
    
    path('Anggota/', Anggota, name='Anggota'),


    path('keuangan/', keuangan, name='keuangan'),
    path('inventaris/', inventaris, name='inventaris'),
    path('surat/', surat, name='surat'),
]

