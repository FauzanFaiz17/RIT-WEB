from django.urls import path
from .views import buat_kegiatan, buat_acara, daftar_kegiatan, daftar_acara, edit_kegiatan, hapus_kegiatan, edit_acara, hapus_acara

urlpatterns = [
    path('buat-kegiatan/', buat_kegiatan, name='buat_kegiatan'),
    path('buat-acara/', buat_acara, name='buat_acara'),
    path('daftar-kegiatan/', daftar_kegiatan, name='daftar_kegiatan'),
    path('daftar-acara/', daftar_acara, name='daftar_acara'),
    path('edit-kegiatan/<int:pk>/', edit_kegiatan, name='edit_kegiatan'),
    path('hapus-kegiatan/<int:pk>/', hapus_kegiatan, name='hapus_kegiatan'),
    path('edit-acara/<int:pk>/', edit_acara, name='edit_acara'),
    path('hapus-acara/<int:pk>/', hapus_acara, name='hapus_acara'),
]