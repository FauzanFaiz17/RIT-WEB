from rest_framework import serializers
from .models import Subtask

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'nama', 'tanggal_mulai', 'tanggal_selesai', 'id_task']
