from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from anuncio.models import Anuncio, Anunciante
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    anuncio = reversed(Anuncio.objects.all())
    busca = request.GET.get('search')
    if busca:
        anuncio = Anuncio.objects.filter(
            Q(nome_modelo__icontains=busca) | Q(nome_marca__icontains=busca) | Q(
                cor__icontains=busca)
        )
    print(busca)
    return render(request, 'site/index.html', {'anuncio': anuncio,
                                               'busca': busca})


def criar(request):
    if request.method == "POST":
        marca = request.POST.get('field-marca')
        modelo = request.POST.get('field-modelo')
        ano = request.POST.get('field-ano')
        combustivel = request.POST.get('combustivel')
        cor = request.POST.get('cor')
        portas = request.POST.get('portas')
        cambio = request.POST.get('cambio')
        ipva = request.POST.get('ipva')
        placa = request.POST.get('placa')
        valor = request.POST.get('valor')
        acendedor_cigarros = request.POST.get('acendedor_cigarros')
        air_bags = request.POST.get('air_bags')
        alarme = request.POST.get('alarme')
        ar_condicionado = request.POST.get('ar_condicionado')
        ar_condicionado_digital = request.POST.get('ar_condicionado_digital')
        ar_condicionado_dual_zone = request.POST.get('ar_condicionado_dual_zone')
        ar_quente = request.POST.get('ar_quente')
        assistente_saida_aclive = request.POST.get('assistente_saida_aclive')
        sistema_audio = request.POST.get('sistema audio')
        banco_apoio_braco = request.POST.get('banco_apoio_banco')
        banco_regulagem_eletrica = request.POST.get('banco_regulagem_eletrica')
        blindado = request.POST.get('blindado')
        bluetooth = request.POST.get('bluetooth')
        calotas = request.POST.get('calotas')
        camera_re = request.POST.get('camera_re')
        carregador_dispositivo_wireless = request.POST.get('carregador_dispositivo_wireless')
        cd_mp3 = request.POST.get('cd_mp3')
        chaves_keyless = request.POST.get('chaves_keyless')
        chaves_sensor_presenca = request.POST.get('chaves_sensor_presenca')
        computador_bordo = request.POST.get('computador_bordo')
        controle_som_volante = request.POST.get('controle_som_volante')
        controle_eletronico_descida = request.POST.get('controle_eletronico_descida')
        desembacador_traseiro = request.POST.get('desembacador_traseiro')
        direcao_eletrica = request.POST.get('direcao_eletrica')
        direcao_hidraulica = request.POST.get('direcao_hidraulica')
        encosto_cabeca_traseiro = request.POST.get('encosto_cabeca_traseiro')
        estribo = request.POST.get('estribo')
        farois_automatico = request.POST.get('farois_automatico')
        farois_milhas = request.POST.get('farois_milhas')
        farois_neblina = request.POST.get('farois_neblina')
        freio_abs = request.POST.get('freio_abs')
        gps = request.POST.get('gps')
        insulfilm = request.POST.get('insulfilm')
        lona_maritima = request.POST.get('lona_maritima')
        multimidia = request.POST.get('multimidia')
        painel_lcd = request.POST.get('painel_lcd')
        painel_digital = request.POST.get('paienl_digital')
        parachoque_cor_veiculo = request.POST.get('parachoque_cor_veiculo')
        park_assist = request.POST.get('park_assist')
        partida_start_stop = request.POST.get('partida_start_stop')
        piloto_automatico = request.POST.get('piloto_automatico')
        pintura_metalica = request.POST.get('pintura_metalica')
        porta_copo = request.POST.get('porta_copo')
        protecao_cacamba = request.POST.get('protecao_cacamba')
        radio = request.POST.get('radio')
        rebatimento_retrovisores_externos = request.POST.get('rebatimento_retrovisores_externos')
        retrovisor_fotocromatico = request.POST.get('retrovisor_fotocromatico')
        retrovisor_interno_eletrocromico = request.POST.get('retrovisor_interno_eletrocromico')
        retrovisor_eletrico = request.POST.get('retrovisor_eletrico')
        roda_liga_leve = request.POST.get('roda_liga_leve')
        sensor_chuva = request.POST.get('sensor_chuva')
        sensor_estacionamento_dianteiro = request.POST.get('sensor_estacionamento_dianteiro')
        sensor_estacionamento_traseiro = request.POST.get('sensor_estacionamento_traseiro')
        teto_solar = request.POST.get('teto_solar')
        teto_panoramico = request.POST.get('teto_panoramico')
        tracao = request.POST.get('tracao')
        trava_eletrica = request.POST.get('trava_eletrica')
        usb = request.POST.get('usb')
        vidro_eletrico = request.POST.get('vidro_eletrico')
        vidro_verdes = request.POST.get('vidro_verdes')
        volante_regulagem_altura = request.POST.get('volante_regulagem_altura')

        anunciado_por = request.user
        Anuncio.objects.create(nome_modelo=modelo,
                               nome_marca=marca,
                               combustivel=combustivel,
                               cor=cor,
                               ano=ano,
                               portas=portas,
                               cambio=cambio,
                               ipva=ipva,
                               placa=placa,
                               valor=valor,
                               acendedor_cigarros=acendedor_cigarros,
                               air_bags=air_bags,
                               alarme=alarme,
                               ar_condicionado=ar_condicionado,
                               ar_condicionado_digital=ar_condicionado_digital,
                               ar_condicionado_dual_zone=ar_condicionado_dual_zone,
                               ar_quente=ar_quente,
                               assistente_saida_aclive=assistente_saida_aclive,
                               sistema_audio=sistema_audio,
                               banco_apoio_braco=banco_apoio_braco,
                               banco_regulagem_eletrica=banco_regulagem_eletrica,
                               blindado=blindado,
                               bluetooth=bluetooth,
                               calotas=calotas,
                               camera_re=camera_re,
                               carregador_dispositivo_wireless=carregador_dispositivo_wireless,
                               cd_mp3=cd_mp3,
                               chaves_keyless=chaves_keyless,
                               chaves_sensor_presenca=chaves_sensor_presenca,
                               computador_bordo=computador_bordo,
                               controle_eletronico_descida=controle_eletronico_descida,
                               controle_som_volante=controle_som_volante,
                               desembacador_traseiro=desembacador_traseiro,
                               direcao_eletrica=direcao_eletrica,
                               direcao_hidraulica=direcao_hidraulica,
                               encosto_cabeca_traseiro=encosto_cabeca_traseiro,
                               estribo=estribo,
                               farois_automatico=farois_automatico,
                               farois_milhas=farois_milhas,
                               farois_neblina=farois_neblina,
                               freio_abs=freio_abs,
                               gps=gps,
                               insulfilm=insulfilm,
                               lona_maritima=lona_maritima,
                               multimidia=multimidia,
                               painel_lcd=painel_lcd,
                               painel_digital=painel_digital,
                               parachoque_cor_veiculo=parachoque_cor_veiculo,
                               park_assist=park_assist,
                               partida_start_stop=partida_start_stop,
                               piloto_automatico=piloto_automatico,
                               pintura_metalica=pintura_metalica,
                               porta_copo=porta_copo,
                               protecao_cacamba=protecao_cacamba,
                               radio=radio,
                               rebatimento_retrovisores_externos=rebatimento_retrovisores_externos,
                               retrovisor_fotocromatico=retrovisor_fotocromatico,
                               retrovisor_interno_eletrocromico=retrovisor_interno_eletrocromico,
                               retrovisor_eletrico=retrovisor_eletrico,
                               roda_liga_leve=roda_liga_leve,
                               sensor_chuva=sensor_chuva,
                               sensor_estacionamento_dianteiro=sensor_estacionamento_dianteiro,
                               sensor_estacionamento_traseiro=sensor_estacionamento_traseiro,
                               teto_solar=teto_solar,
                               teto_panoramico=teto_panoramico,
                               tracao=tracao,
                               trava_eletrica=trava_eletrica,
                               usb=usb,
                               vidro_eletrico=vidro_eletrico,
                               vidro_verdes=vidro_verdes,
                               volante_regulagem_altura=volante_regulagem_altura,

                               anunciado_por=anunciado_por)
        return redirect('index')
    return render(request, 'site/anunciar.html')


def editar(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    if request.method == "POST":
        modelo = request.POST.get('nome_modelo')
        marca = request.POST.get('nome_marca')
        cor = request.POST.get('cor')
        Anuncio.objects.filter(pk=pk).update(nome_modelo=modelo, nome_marca=marca, cor=cor)
        return redirect('index')
    else:
        return render(request, 'site/editar.html', {'anuncio': anuncio})


def deletar(request, pk):
    anuncio = get_object_or_404(Anuncio, pk=pk)
    anuncio.delete()
    return redirect('index')


def criar_user(request):
    if request.method == "POST":
        user = request.POST.get('nome_user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        novoUsuario = User.objects.create_user(username=user, email=email, password=password)
        novoUsuario.save()
        return redirect(reverse('area-anunciantes', args=[novoUsuario.pk]))
    else:
        return render(request, 'site/criar-user.html')


def area_anunciantes(request, pk):
    anunciante = User.objects.filter(pk=pk)
    token = Token.objects.filter(user=pk)
    print(token)
    return render(request, 'site/lista-anunciantes.html', {'anunciantes': anunciante,
                                                           'token': token})


def criar_token(request):
    token = Token.objects.create(User)
    Anunciante.objects.create(user_anunciante=user, user_email=email, password_anunciante=password, token_api=token)
    return redirect(lista_anunciantes)
