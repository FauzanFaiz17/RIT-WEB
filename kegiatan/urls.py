from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import register, user_login, user_logout, dashboard, icons, map, profile, tables, struktur, it_com, web_dev, events, tambah_kegiatan, hapus_kegiatan, edit_kegiatan, projek_manage

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
    path('struktur/it_com', it_com, name='it_com'),
    path('struktur/it_com/web_dev', web_dev, name='web_dev'),
    path('events/', events, name='events'),
    path('events/tambah_kegiatan', tambah_kegiatan, name='tambah_kegiatan'),
    path('kegiatan/delete/<int:id>/', hapus_kegiatan, name='hapus_kegiatan'),
    path('kegiatan/edit/<int:id>/', edit_kegiatan, name='edit_kegiatan'),
    path('projek_manage/', projek_manage, name='projek_manage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)