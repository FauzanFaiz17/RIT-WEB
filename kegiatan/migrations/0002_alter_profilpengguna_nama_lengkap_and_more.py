# Generated by Django 5.1.2 on 2025-01-08 13:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilpengguna',
            name='nama_lengkap',
            field=models.CharField(blank=True, default='Tidak Diisi', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilpengguna',
            name='no_hp',
            field=models.CharField(blank=True, default='0000000000', max_length=15),
        ),
        migrations.AlterField(
            model_name='profilpengguna',
            name='npm',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profilpengguna',
            name='prodi',
            field=models.CharField(blank=True, default='Tidak Diisi', max_length=100),
        ),
        migrations.AlterField(
            model_name='profilpengguna',
            name='semester',
            field=models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(14)]),
        ),
    ]
