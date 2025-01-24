from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models

class ProfilPengguna(AbstractUser):
    PRODI_CHOICES = [
    ("TI", "Teknologi Informasi"),
    ("RPL", "Rekayasa Perangkat Lunak"),
    ("RSK", "Rekayasa Sistem Komputer"),
]
    namadepan = models.CharField(max_length=50)
    namabelakang = models.CharField(max_length=50)
    no_hp = models.CharField(max_length=15)
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
    
    def _str_(self):
        return f"{self.nama_lengkap}"

    class Meta:
        verbose_name = "Profil Pengguna"
        verbose_name_plural = "Profil Pengguna"


class Komunitas(models.Model):
    nama = models.CharField(max_length=100)
    kepala = models.ForeignKey(ProfilPengguna, on_delete=models.SET_NULL, null=True, related_name='kepala_komunitas')
    anggota = models.ManyToManyField(ProfilPengguna, related_name='anggota_komunitas', blank=True)
    deskripsi = models.TextField(blank=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Komunitas"
        verbose_name_plural = "Komunitas"

class Divisi(models.Model):
    nama = models.CharField(max_length=100)
    komunitas = models.ForeignKey(Komunitas, on_delete=models.CASCADE, related_name='divisi')
    kepala = models.ForeignKey(ProfilPengguna, on_delete=models.SET_NULL, null=True, related_name='kepala_divisi')
    anggota = models.ManyToManyField(ProfilPengguna, related_name='anggota_divisi', blank=True)

    def __str__(self):
        return f"{self.nama} ({self.komunitas.nama})"
    
    class Meta:
        verbose_name = "Divisi"
        verbose_name_plural = "Divisi"

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

<<<<<<< HEAD
class Project(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    kepala = models.ForeignKey(ProfilPengguna, on_delete=models.SET_NULL, null=True, related_name='kepala_project')
    divisi = models.ForeignKey('Divisi', on_delete=models.CASCADE, related_name='projects')
    
    def __str__(self):
        return self.nama

class Taks(models.Model):
    nama = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    status = models.CharField(max_length=20, choices=[('belum', 'Belum Dikerjakan'), ('proses', 'Dalam Proses'), ('selesai', 'Selesai')])
    
    def clean(self):
        if self.tanggal_selesai < self.tanggal_mulai:
            raise ValidationError("Tanggal selesai tidak boleh lebih awal dari tanggal mulai")
    
    def __str__(self):
        return f"{self.nama} (Project: {self.project.nama})"

class SubTaks(models.Model):
    nama = models.CharField(max_length=100)
    taks = models.ForeignKey(Taks, on_delete=models.CASCADE, related_name='subtasks')
    pengguna = models.ForeignKey(ProfilPengguna, on_delete=models.CASCADE, related_name='subtasks')
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    status = models.CharField(max_length=20, choices=[('belum', 'Belum Dikerjakan'), ('proses', 'Dalam Proses'), ('selesai', 'Selesai')])
    laporan_path = models.FileField(upload_to='laporan_subtasks/', blank=True, null=True)
    
    def clean(self):
        if self.tanggal_selesai < self.tanggal_mulai:
            raise ValidationError("Tanggal selesai tidak boleh lebih awal dari tanggal mulai")
    
    def __str__(self):
        return f"{self.nama} (Taks: {self.taks.nama})"
=======
class Task(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    pengguna = models.ForeignKey('ProfilPengguna', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


class SubTask(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()

    def clean(self):
        # Validasi tanggal
        if self.tanggal_selesai < self.tanggal_mulai:
            raise ValidationError("Tanggal selesai tidak boleh lebih awal dari tanggal mulai")

    def __str__(self):
        return f"{self.nama} (Task: {self.task.nama})"

    class Meta:
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"
>>>>>>> c1feb86b07a1247b65ed685e7483788812e2b85d
