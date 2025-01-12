from django.contrib import admin
from .models import ProfilPengguna, Kegiatan, Komunitas, Divisi, Gambar

class ProfilPenggunaAdmin(admin.ModelAdmin):
    # Field yang akan ditampilkan di daftar pengguna di admin
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'nama_lengkap', 'npm')

    # Mengatur field yang bisa diedit di halaman detail user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('nama_lengkap', 'email', 'no_hp', 'prodi', 'semester', 'npm', 'tanggal_lahir', 'foto_profil')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Tambahkan field tambahan Anda ke form pendaftaran pengguna di admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'nama_lengkap', 'email', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )

admin.site.register(ProfilPengguna, ProfilPenggunaAdmin)
admin.site.register(Kegiatan)
admin.site.register(Divisi)
admin.site.register(Komunitas)