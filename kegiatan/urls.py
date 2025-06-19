# kegiatan/urls.py

from django.urls import path
from .views import kegiatan, tambah_kegiatan, edit_kegiatan, hapus_kegiatan, hapus_foto_kegiatan , acara, tambah_acara, edit_acara, hapus_acara, hapus_foto_acara

urlpatterns = [
    path('', kegiatan, name='kegiatan'),
    path('tambah/', tambah_kegiatan, name='tambah_kegiatan'),
    path('<int:pk>/edit/', edit_kegiatan, name='edit_kegiatan'),
    path('<int:pk>/delete/', hapus_kegiatan, name='hapus_kegiatan'),
    path('foto/<int:pk>/hapus/', hapus_foto_kegiatan, name='hapus_foto_kegiatan'),

    path('acara/', acara, name='acara'),
    path('acara/tambah/', tambah_acara, name='tambah_acara'),
    path('acara/<int:pk>/edit/', edit_acara, name='edit_acara'),
    path('acara/<int:pk>/delete/', hapus_acara, name='hapus_acara'),
    path('acara/foto/<int:pk>/hapus/', hapus_foto_acara, name='hapus_foto_acara'),
]
