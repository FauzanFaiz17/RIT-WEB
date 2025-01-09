from django.contrib import admin
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

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'pengguna')  # Kolom yang ditampilkan di daftar admin
    search_fields = ('nama', 'pengguna__namadepan', 'pengguna__namabelakang')  # Pencarian
    list_filter = ('pengguna',)  # Filter berdasarkan pengguna
    ordering = ('id',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'task', 'tanggal_mulai', 'tanggal_selesai')
    search_fields = ('nama', 'task__nama')  # Pencarian
    list_filter = ('task', 'tanggal_mulai')  # Filter berdasarkan task dan tanggal
    ordering = ('id',)