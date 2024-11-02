from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('kegiatan/', views.daftar_kegiatan, name='daftar_kegiatan'),
    path('kegiatan/tambah/', views.tambah_kegiatan, name='tambah_kegiatan'),
]

# Menyajikan file media selama pengembangan
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)