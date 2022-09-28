from rest_framework import serializers
from anuncio.models import Anuncio


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ['id', 'nome_modelo', 'nome_marca', 'cor']
