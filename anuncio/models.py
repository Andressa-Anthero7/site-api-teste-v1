from django.db import models

# Create your models here.


class Anuncio(models.Model):
    tipo_veiculo = models.CharField(max_length=100)
    nome_marca = models.CharField(max_length=100)
    nome_modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)


