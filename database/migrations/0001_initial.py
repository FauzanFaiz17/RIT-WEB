# Generated by Django 5.1.4 on 2025-01-24 08:33

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Divisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Divisi',
                'verbose_name_plural': 'Divisi',
            },
        ),
        migrations.CreateModel(
            name='Komunitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Komunitas',
                'verbose_name_plural': 'Komunitas',
            },
        ),
        migrations.CreateModel(
            name='Kegiatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(blank=True)),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField()),
                ('status', models.CharField(choices=[('terlaksana', 'Terlaksana'), ('sedang_terlaksana', 'Sedang Terlaksana'), ('tidak_terlaksana', 'Tidak Terlaksana'), ('belum_terlaksana', 'Belum Terlaksana')], max_length=20)),
                ('jenis', models.CharField(choices=[('kegiatan', 'Kegiatan'), ('acara', 'Acara')], max_length=20)),
                ('divisi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kegiatan', to='database.divisi')),
                ('komunitas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kegiatan', to='database.komunitas')),
            ],
            options={
                'verbose_name': 'Kegiatan',
                'verbose_name_plural': 'Kegiatan',
            },
        ),
        migrations.CreateModel(
            name='Gambar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(upload_to='gambar_kegiatan/')),
                ('kegiatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gambar', to='database.kegiatan')),
            ],
            options={
                'verbose_name': 'Gambar',
                'verbose_name_plural': 'Gambar',
            },
        ),
        migrations.AddField(
            model_name='divisi',
            name='komunitas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisi', to='database.komunitas'),
        ),
        migrations.CreateModel(
            name='ProfilPengguna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('namadepan', models.CharField(max_length=50)),
                ('namabelakang', models.CharField(max_length=50)),
                ('no_hp', models.CharField(max_length=15)),
                ('prodi', models.CharField(blank=True, choices=[('TI', 'Teknologi Informasi'), ('RPL', 'Rekayasa Perangkat Lunak'), ('RSK', 'Rekayasa Sistem Komputer')], default='TI', max_length=50)),
                ('semester', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(14)])),
                ('npm', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('foto_profil', models.ImageField(blank=True, null=True, upload_to='foto_profil/')),
                ('tanggal_lahir', models.DateField(blank=True, null=True)),
                ('jabatan', models.CharField(blank=True, default='Tidak Diisi', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='profilpengguna_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='profilpengguna_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Profil Pengguna',
                'verbose_name_plural': 'Profil Pengguna',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='komunitas',
            name='anggota',
            field=models.ManyToManyField(blank=True, related_name='anggota_komunitas', to='database.profilpengguna'),
        ),
        migrations.AddField(
            model_name='komunitas',
            name='kepala',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kepala_komunitas', to='database.profilpengguna'),
        ),
        migrations.AddField(
            model_name='divisi',
            name='anggota',
            field=models.ManyToManyField(blank=True, related_name='anggota_divisi', to='database.profilpengguna'),
        ),
        migrations.AddField(
            model_name='divisi',
            name='kepala',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kepala_divisi', to='database.profilpengguna'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(blank=True)),
                ('pengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='database.profilpengguna')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(blank=True)),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='database.task')),
            ],
            options={
                'verbose_name': 'SubTask',
                'verbose_name_plural': 'SubTasks',
            },
        ),
    ]
