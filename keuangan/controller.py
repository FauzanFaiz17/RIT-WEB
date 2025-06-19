from .models import Keuangan

def hitung_sisa_keuangan():
    keuangans = Keuangan.objects.order_by('tanggal', 'id')
    sisa = 0
    for k in keuangans:
        if k.jenis == 'masuk':
            sisa += k.jumlah
        else:
            sisa -= k.jumlah
        k.sisa = sisa
        k.save(update_fields=['sisa'])