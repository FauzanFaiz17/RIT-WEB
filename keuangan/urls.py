from django.urls import path
from .views import keuangan, tambah_keuangan, edit_keuangan, hapus_keuangan

urlpatterns = [
    path('', keuangan, name='keuangan'),
    path('tambah/', tambah_keuangan, name='tambah_keuangan'),
    path('<int:pk>/edit/', edit_keuangan, name='edit_keuangan'),
    path('<int:pk>/hapus/', hapus_keuangan, name='hapus_keuangan'),
]