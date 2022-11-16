from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class Anuncio(models.Model):
    nome_marca = models.CharField(max_length=100, blank=False, null=False)
    nome_modelo = models.CharField(max_length=100, blank=False, null=False)
    ano = models.CharField(max_length=4, blank=False, null=False)
    combustivel = models.CharField(max_length=10, blank=True, null=True)
    cambio = models.CharField(max_length=10, blank=True, null=True)
    cor = models.CharField(max_length=20, blank=True, null=True)
    portas = models.CharField(max_length=10, blank=True, null=True)
    ipva = models.CharField(max_length=10, blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    valor = models.CharField(max_length=10, blank=False, null=False)
    acendedor_cigarros = models.CharField(max_length=50, blank=True, null=True)
    air_bags = models.CharField(max_length=10, blank=True, null=True)
    alarme = models.CharField(max_length=10, blank=True, null=True)
    ar_condicionado = models.CharField(max_length=20, blank=True, null=True)
    ar_condicionado_digital = models.CharField(max_length=30, blank=True, null=True)
    ar_condicionado_dual_zone = models.CharField(max_length=30, blank=True, null=True)
    ar_quente = models.CharField(max_length=30, blank=True, null=True)
    assistente_saida_aclive = models.CharField(max_length=30, blank=True, null=True)
    sistema_audio = models.CharField(max_length=30, blank=True, null=True)
    banco_apoio_braco =  models.CharField(max_length=30, blank=True, null=True)
    banco_regulagem_eletrica = models.CharField(max_length=30, blank=True, null=True)
    blindado = models.CharField(max_length=30, blank=True, null=True)
    bluetooth = models.CharField(max_length=30, blank=True, null=True)
    calotas = models.CharField(max_length=30, blank=True, null=True)
    camera_re = models.CharField(max_length=30, blank=True, null=True)
    carregador_dispositivo_wireless = models.CharField(max_length=50, blank=True, null=True)
    cd_mp3 = models.CharField(max_length=30, blank=True, null=True)
    chaves_keyless = models.CharField(max_length=30, blank=True, null=True)
    chaves_sensor_presenca = models.CharField(max_length=30, blank=True, null=True)
    computador_bordo = models.CharField(max_length=30, blank=True, null=True)
    controle_som_volante = models.CharField(max_length=30, blank=True, null=True)
    controle_eletronico_descida = models.CharField(max_length=20, blank=True, null=True)
    desembacador_traseiro = models.CharField(max_length=30, blank=True, null=True)
    direcao_eletrica = models.CharField(max_length=30, blank=True, null=True)
    direcao_hidraulica = models.CharField(max_length=30, blank=True, null=True)
    encosto_cabeca_traseiro = models.CharField(max_length=30, blank=True, null=True)
    estribo = models.CharField(max_length=30, blank=True, null=True)
    farois_automatico = models.CharField(max_length=30, blank=True, null=True)
    farois_milhas = models.CharField(max_length=30, blank=True, null=True)
    farois_neblina = models.CharField(max_length=30, blank=True, null=True)
    freio_abs = models.CharField(max_length=30, blank=True, null=True)
    gps = models.CharField(max_length=30, blank=True, null=True)
    insulfilm = models.CharField(max_length=30, blank=True, null=True)
    lona_maritima = models.CharField(max_length=30, blank=True, null=True)
    multimidia = models.CharField(max_length=30, blank=True, null=True)
    painel_lcd = models.CharField(max_length=30, blank=True, null=True)
    painel_digital = models.CharField(max_length=30, blank=True, null=True)
    parachoque_cor_veiculo = models.CharField(max_length=30, blank=True, null=True)
    park_assist = models.CharField(max_length=30, blank=True, null=True)
    partida_start_stop = models.CharField(max_length=30, blank=True, null=True)
    piloto_automatico = models.CharField(max_length=30, blank=True, null=True)
    pintura_metalica = models.CharField(max_length=30, blank=True, null=True)
    porta_copo = models.CharField(max_length=30, blank=True, null=True)
    protecao_cacamba = models.CharField(max_length=30, blank=True, null=True)
    radio = models.CharField(max_length=30, blank=True, null=True)
    rebatimento_retrovisores_externos = models.CharField(max_length=30, blank=True, null=True)
    retrovisor_fotocromatico = models.CharField(max_length=30, blank=True, null=True)
    retrovisor_interno_eletrocromico = models.CharField(max_length=30, blank=True, null=True)
    retrovisor_eletrico = models.CharField(max_length=30, blank=True, null=True)
    roda_liga_leve = models.CharField(max_length=30, blank=True, null=True)
    sensor_chuva = models.CharField(max_length=30, blank=True, null=True)
    sensor_estacionamento_dianteiro = models.CharField(max_length=30, blank=True, null=True)
    sensor_estacionamento_traseiro = models.CharField(max_length=30, blank=True, null=True)
    teto_solar = models.CharField(max_length=30, blank=True, null=True)
    teto_panoramico = models.CharField(max_length=30, blank=True, null=True)
    tracao = models.CharField(max_length=30, blank=True, null=True)
    trava_eletrica = models.CharField(max_length=30, blank=True, null=True)
    usb = models.CharField(max_length=30, blank=True, null=True)
    vidro_eletrico = models.CharField(max_length=30, blank=True, null=True)
    vidro_verdes = models.CharField(max_length=30, blank=True, null=True)
    volante_regulagem_altura = models.CharField(max_length=30, blank=True, null=True)
    info_complementares = models.CharField(max_length=255, blank=True, null=True)
    anunciado_por = models.CharField(max_length=100, blank=True, null=True)




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Anunciante(models.Model):
    user_anunciante = models.CharField(max_length=256)
    email_anunciante = models.CharField(max_length=256)
    password_anunciante = models.CharField(max_length=256)
    token_api = models.CharField(max_length=256)
