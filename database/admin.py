from django.contrib import admin
from .models import ProfilPengguna, Komunitas, Divisi, Kegiatan, Gambar, Backlog

@admin.register(ProfilPengguna)
class ProfilPenggunaAdmin(admin.ModelAdmin):
    list_display = ('namadepan', 'namabelakang', 'npm', 'prodi', 'semester')
    search_fields = ('namadepan', 'namabelakang', 'npm')

@admin.register(Komunitas)
class KomunitasAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kepala')
    search_fields = ('nama',)
    filter_horizontal = ('anggota',)  # Tambahkan widget untuk memilih anggota

@admin.register(Divisi)
class DivisiAdmin(admin.ModelAdmin):
    list_display = ('nama', 'komunitas', 'kepala')
    search_fields = ('nama', 'komunitas__nama')
    filter_horizontal = ('anggota',)  # Tambahkan widget untuk memilih anggota

@admin.register(Kegiatan)
class KegiatanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'status', 'jenis', 'tanggal_mulai', 'tanggal_selesai')
    list_filter = ('status', 'jenis', 'divisi', 'komunitas')
    search_fields = ('nama', 'deskripsi')
    
@admin.register(Gambar)
class GambarAdmin(admin.ModelAdmin):
    list_display = ('kegiatan',)
    search_fields = ('kegiatan__nama',)

@admin.register(Backlog)
class BacklogAdmin(admin.ModelAdmin):
    list_display = ('nama', 'pengguna', 'tanggal_mulai', 'tanggal_selesai')
    search_fields = ('nama', 'pengguna__namadepan', 'pengguna__namabelakang')
