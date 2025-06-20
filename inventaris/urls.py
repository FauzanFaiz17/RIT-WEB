from django.urls import path
from .views import barang,barang_create,barang_delete,barang_update , hapus_foto_barang

urlpatterns = [
    path('', barang, name='barang'),
    path('tambah/', barang_create, name='tambah_barang'),
    path('edit/<int:pk>/', barang_update, name='barang_update'),
    path('hapus/<int:pk>/', barang_delete, name='barang_delete'),
    path('<int:pk>/', hapus_foto_barang, name='hapus_foto_barang'),
]
