from django.contrib import admin
from .models import ProfilPengguna, Komunitas, Divisi, Kegiatan, Gambar, Project, Taks, SubTaks
from .models import ProfilPengguna, Komunitas, Divisi, Kegiatan, Gambar, Task, SubTask

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

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'kepala', 'divisi')
    search_fields = ('nama', 'kepala__namadepan', 'kepala__namabelakang')
    list_filter = ('divisi', 'kepala')
    ordering = ('id',)

@admin.register(Taks)
class TaksAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'project', 'tanggal_mulai', 'tanggal_selesai', 'status')
    search_fields = ('nama', 'project__nama')
    list_filter = ('project', 'status', 'tanggal_mulai')
    ordering = ('id',)

@admin.register(SubTaks)
class SubTaksAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'taks', 'pengguna', 'tanggal_mulai', 'tanggal_selesai', 'status')
    search_fields = ('nama', 'taks__nama', 'pengguna__namadepan', 'pengguna__namabelakang')
    list_filter = ('taks', 'status', 'tanggal_mulai')
    ordering = ('id',)