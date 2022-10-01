from rest_framework import viewsets
from anuncio.models import Anuncio
from anuncio.serializer import AnuncioSerializer
from rest_framework.permissions import IsAuthenticated


class AnunciosViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer
