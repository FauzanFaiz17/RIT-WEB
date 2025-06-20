from django.urls import path
from .views import surat, tambah_surat,edit_surat,delete_surat

urlpatterns = [
    path('', surat, name='surat'),
    path('tambah/', tambah_surat, name='tambah_surat'),
    path('edit/<int:pk>/', edit_surat, name='edit_surat'),
    path('<int:pk>/hapus/', delete_surat, name='delete_surat'),
]