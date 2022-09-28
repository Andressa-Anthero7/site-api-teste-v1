from rest_framework import viewsets
from anuncio.models import Anuncio
from anuncio.serializer import AnuncioSerializer


class AnunciosViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
