# Generated by Django 5.1.2 on 2025-01-26 12:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0008_remove_task_deskripsi_remove_task_pengguna_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('tanggal_mulai', models.DateField(blank=True, null=True)),
                ('tanggal_selesai', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('selesai', 'selesai'), ('sedang_dikerjakan', 'Sedang Dikerjakan'), ('tidak_dikerjakan', 'Tidak Dikerjakan'), ('belum_dikerjakan', 'Belum Dikerjakan')], max_length=20, null=True)),
                ('id_profilepengguna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtask', to=settings.AUTH_USER_MODEL)),
                ('id_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='kegiatan.task')),
            ],
        ),
    ]
