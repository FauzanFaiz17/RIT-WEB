from django.core.management.base import BaseCommand
from kegiatan.models import Kegiatan, GambarKegiatan

class Command(BaseCommand):
    help = 'Seed the database with example data'

    def handle(self, *args, **kwargs):
        Kegiatan.objects.all().delete()
        GambarKegiatan.objects.all().delete()

        kegiatan3 = Kegiatan.objects.create(
            nama='Kegiatan 1',
            deskripsi='Deskripsi untuk Kegiatan 1',
            tanggal='2024-11-05'
        )

        kegiatan4 = Kegiatan.objects.create(
            nama='Kegiatan 2',
            deskripsi='Deskripsi untuk Kegiatan 2',
            tanggal='2024-11-10'
        )

        # Pastikan gambar sudah ada di folder media
        GambarKegiatan.objects.create(kegiatan=kegiatan3, gambar='IMG-20240916-WA0487.jpg')
        GambarKegiatan.objects.create(kegiatan=kegiatan3, gambar='WhatsApp Image 2024-10-24 at 13.11.38.jpeg')
        GambarKegiatan.objects.create(kegiatan=kegiatan4, gambar='WhatsApp Image 2024-10-24 at 13.11.38.jpeg')

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
