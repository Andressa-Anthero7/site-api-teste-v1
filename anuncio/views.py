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
        marca = request.POST.get('nome_marca')
        modelo = request.POST.get('nome_modelo')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')
        anunciado_por = request.user
        Anuncio.objects.create(nome_modelo=modelo, nome_marca=marca, cor=cor, ano=ano, anunciado_por=anunciado_por)
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
