from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class Anuncio(models.Model):
    nome_marca = models.CharField(max_length=100)
    nome_modelo = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)
    cor = models.CharField(max_length=100)
    anunciado_por = models.CharField(max_length=100)

    def __str__(self):
        return self.pk


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Anunciante(models.Model):
    user_anunciante = models.CharField(max_length=256)
    email_anunciante = models.CharField(max_length=256)
    password_anunciante = models.CharField(max_length=256)
    token_api = models.CharField(max_length=256)
