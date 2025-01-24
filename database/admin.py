from django.contrib import admin
<<<<<<< HEAD
from .models import ProfilPengguna, Komunitas, Divisi, Kegiatan, Gambar, Project, Taks, SubTaks
=======
from .models import ProfilPengguna, Komunitas, Divisi, Kegiatan, Gambar, Task, SubTask
>>>>>>> c1feb86b07a1247b65ed685e7483788812e2b85d

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

<<<<<<< HEAD
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
=======
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
>>>>>>> c1feb86b07a1247b65ed685e7483788812e2b85d
