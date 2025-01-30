from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import register, user_login, user_logout, get_subtasks , dashboard, profile, struktur, it_com, web_dev, events, tambah_kegiatan, hapus_kegiatan, edit_kegiatan, projek_manage, gm_com, game_dev, iot_div, keanggotaan, hapus_projek, projek_proses, edit_subtask, edit_task

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('login/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('struktur/', struktur, name='struktur'),
    path('struktur/it_com', it_com, name='it_com'),
    path('struktur/gm_com', gm_com, name='gm_com'),
    path('struktur/it_com/web_dev', web_dev, name='web_dev'),
    path('struktur/it_com/game_dev', game_dev, name='game_dev'),
    path('struktur/it_com/iot_div', iot_div, name='iot_div'),
    path('struktur/it_com/keanggotaan', keanggotaan, name='keanggotaan'),
    path('events/', events, name='events'),
    path('events/tambah_kegiatan', tambah_kegiatan, name='tambah_kegiatan'),
    path('kegiatan/delete/<int:id>/', hapus_kegiatan, name='hapus_kegiatan'),
    path('projek_manage/delete/<int:id>/', hapus_projek, name='hapus_projek'),
    path('edit_subtask/<int:id>/', edit_subtask, name='edit_subtask'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
    path('projek_manage/proses/<int:id>/', projek_proses, name='projek_proses'),
    path('kegiatan/edit/<int:id>/', edit_kegiatan, name='edit_kegiatan'),
    path('projek_manage/', projek_manage, name='projek_manage'),
    path('api/subtasks/<int:project_id>/', get_subtasks, name='api_subtasks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)