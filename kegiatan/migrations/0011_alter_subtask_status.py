# Generated by Django 5.1.2 on 2025-01-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0010_alter_subtask_id_profilepengguna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='status',
            field=models.CharField(blank=True, choices=[('selesai', 'selesai'), ('sedang_dikerjakan', 'Sedang Dikerjakan'), ('belum_dikerjakan', 'Belum Dikerjakan')], default='belum_dikerjakan', max_length=20, null=True),
        ),
    ]
