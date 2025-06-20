# urls.py
from django.urls import path
from .views import keuangan, tambah_keuangan, edit_keuangan, hapus_keuangan,hapus_foto_keuangan

urlpatterns = [
    path('', keuangan, name='keuangan'),
    path('tambah/', tambah_keuangan, name='tambah_keuangan'),
    path('<int:pk>/edit/', edit_keuangan, name='edit_keuangan'),
    path('<int:pk>/hapus/', hapus_keuangan, name='hapus_keuangan'),
    path('foto/<int:foto_id>/hapus/', hapus_foto_keuangan, name='hapus_foto_keuangan'),

]
