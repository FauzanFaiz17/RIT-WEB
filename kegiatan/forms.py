from django import forms
from .models import Kegiatan

class KegiatanForm(forms.ModelForm):
    class Meta:
        model = Kegiatan
        fields = ['nama', 'deskripsi', 'tanggal', 'status', 'ketua_pelaksana', 'komunitas']

    def __init__(self, *args, **kwargs):
        super(KegiatanForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field in ['status', 'komunitas', 'ketua_pelaksana']:
                self.fields[field].widget.attrs.update({'class': 'form-select'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
