from django.contrib import admin
from .models import User, Komunitas, Divisi, AnggotaDivisi

admin.site.register(User)
admin.site.register(Komunitas)
admin.site.register(Divisi)
admin.site.register(AnggotaDivisi)
