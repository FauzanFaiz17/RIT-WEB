from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models

class Komunitas(models.Model):
    nama = models.CharField(max_length=100)
    kepala = models.ForeignKey('ProfilPengguna', on_delete=models.SET_NULL, blank=True, null=True, related_name='kepala_komunitas')
    anggota = models.ManyToManyField('ProfilPengguna', related_name='anggota_komunitas', blank=True)
    deskripsi = models.TextField(blank=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Komunitas"
        verbose_name_plural = "Komunitas"

class Divisi(models.Model):
    nama = models.CharField(max_length=100)
    komunitas = models.ForeignKey(Komunitas, on_delete=models.CASCADE, related_name='divisi')
    kepala = models.ForeignKey('ProfilPengguna', on_delete=models.SET_NULL, blank=True, null=True, related_name='kepala_divisi')
    anggota = models.ManyToManyField('ProfilPengguna', related_name='anggota_divisi', blank=True)

    def __str__(self):
        return f"{self.nama} ({self.komunitas.nama})"
    
    class Meta:
        verbose_name = "Divisi"
        verbose_name_plural = "Divisi"

# Model ProfilPengguna tetap berada di bawah
class ProfilPengguna(AbstractUser):
    PRODI_CHOICES = [
        ("TI", "Teknologi Informasi"),
        ("RPL", "Rekayasa Perangkat Lunak"),
        ("RSK", "Rekayasa Sistem Komputer"),
    ]

    nama_lengkap = models.CharField(max_length=100, blank=True, default="Tidak Diisi")
    no_hp = models.CharField(max_length=15, blank=True, default="0000000000")
    prodi = models.CharField(
        max_length=50,
        choices=PRODI_CHOICES,
        blank=True,
        default="TI"
    )
    semester = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(14)],
        blank=True,
        null=True,
        default=1,
    )
    npm = models.CharField(max_length=15, unique=True, blank=True, null=True)
    foto_profil = models.ImageField(upload_to="foto_profil/", blank=True, null=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    jabatan = models.CharField(max_length=100, blank=True, default="Tidak Diisi")  # Field baru
    komunitas = models.ForeignKey(Komunitas, on_delete=models.SET_NULL, null=True, blank=True)
    divisi = models.ForeignKey(Divisi, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        Group,
        related_name="profilpengguna_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="profilpengguna_set",
        blank=True,
    )

    def __str__(self):
        return f"{self.nama_lengkap}"

    class Meta:
        verbose_name = "Profil Pengguna"
        verbose_name_plural = "Profil Pengguna"

class Kegiatan(models.Model):
    STATUS_CHOICES = [
        ('terlaksana', 'Terlaksana'),
        ('sedang_terlaksana', 'Sedang Terlaksana'),
        ('tidak_terlaksana', 'Tidak Terlaksana'),
        ('belum_terlaksana', 'Belum Terlaksana'),
    ]
    
    JENIS_CHOICES = [
        ('kegiatan', 'Kegiatan'),
        ('acara', 'Acara'),
    ]
    nama = models.CharField(max_length=100)
    divisi = models.ForeignKey(
        Divisi, on_delete=models.CASCADE, related_name='kegiatan', blank=True, null=True
    )  # Divisi opsional
    komunitas = models.ForeignKey(
        Komunitas, on_delete=models.CASCADE, related_name='kegiatan', blank=True, null=True
    )  # Komunitas opsional
    deskripsi = models.TextField(blank=True)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    jenis = models.CharField(max_length=20, choices=JENIS_CHOICES)
    
    def clean(self):
        # Validasi tanggal
        if self.tanggal_selesai < self.tanggal_mulai:
            raise ValidationError("Tanggal selesai tidak boleh lebih awal dari tanggal mulai")
        # Validasi minimal satu penyelenggara
        if not self.divisi and not self.komunitas:
            raise ValidationError("Minimal salah satu penyelenggara (Divisi atau Komunitas) harus diisi")
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Kegiatan"
        verbose_name_plural = "Kegiatan"

class Gambar(models.Model):
    kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE, related_name='gambar')
    gambar = models.ImageField(upload_to='gambar_kegiatan/')

    def __str__(self):
        return f"gambar untuk {self.kegiatan.nama}"
    
    class Meta:
        verbose_name = "Gambar"
        verbose_name_plural = "Gambar"

class Project(models.Model):
    STATUS_CHOICES = [
        ('belum_dikerjakan', 'Belum Dikerjakan'),
        ('sedang_dikerjakan', 'Sedang Dikerjakan'),
        ('selesai', 'Selesai'),
    ]
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    nama_kepala = models.ForeignKey(ProfilPengguna, on_delete=models.CASCADE, related_name='project')
    divisi = models.ForeignKey(
        Divisi, on_delete=models.CASCADE, related_name='project', blank=True, null=True
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='belum_dikerjakan',
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project"

class Task(models.Model):
    STATUS_CHOICES = [
        ('selesai', 'selesai'),
        ('sedang_dikerjakan', 'Sedang Dikerjakan'),
        ('belum_dikerjakan', 'Belum Dikerjakan'),
    ]
    nama = models.CharField(max_length=100)
    tanggal_mulai = models.DateField(blank=True, null=True)
    tanggal_selesai = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='belum_dikerjakan',
        blank=True, 
        null=True
    )
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def save(self, *args, **kwargs):
        is_new = self.pk is None  # Cek apakah ini objek baru
        super(Task, self).save(*args, **kwargs)  # ⬅️ Save DULU agar ID tersedia

        if not is_new:  # Hanya jalankan jika Task sudah ada
            subtask = self.subtask.all()
            
            if subtask.exists():
                self.tanggal_mulai = subtask.order_by('tanggal_mulai').first().tanggal_mulai
                self.tanggal_selesai = subtask.order_by('-tanggal_selesai').first().tanggal_selesai

                if subtask.filter(status='belum_dikerjakan').exists():
                    self.status = 'sedang_dikerjakan'
                elif subtask.filter(status='sedang_dikerjakan').exists():
                    self.status = 'sedang_dikerjakan'
                else:
                    self.status = 'selesai'
            else:
                self.tanggal_mulai = None
                self.tanggal_selesai = None
                self.status = 'belum_dikerjakan'

            super(Task, self).save(update_fields=['tanggal_mulai', 'tanggal_selesai', 'status'])

class Subtask(models.Model):
    STATUS_CHOICES = [
        ('selesai', 'selesai'),
        ('sedang_dikerjakan', 'Sedang Dikerjakan'),
        ('belum_dikerjakan', 'Belum Dikerjakan'),
    ]
    nama = models.CharField(max_length=100)
    tanggal_mulai = models.DateField(blank=True, null=True)
    tanggal_selesai = models.DateField(blank=True, null=True) 
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='belum_dikerjakan',
        blank=True, 
        null=True
    )
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtask', blank=True, null=True)
    id_profilepengguna = models.ForeignKey(ProfilPengguna, on_delete=models.CASCADE, related_name='subtask', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Update status berdasarkan tanggal mulai dan selesai
        if self.tanggal_selesai:
            self.status = 'selesai'
        elif self.tanggal_mulai:
            self.status = 'sedang_dikerjakan'
        else:
            self.status = 'belum_dikerjakan'

        super(Subtask, self).save(*args, **kwargs)

        # Setelah menyimpan subtask, update task terkait
        if self.id_task:
            self.id_task.save()
