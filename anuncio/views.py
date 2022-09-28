from django.shortcuts import render, redirect, get_object_or_404
from anuncio.models import Anuncio


# Create your views here.

def index(request):
    anuncio = reversed(Anuncio.objects.all())
    return render(request, 'site/index.html', {'anuncio': anuncio})


def criar(request):
    if request.method == "POST":
        modelo = request.POST.get('nome_modelo')
        marca = request.POST.get('nome_marca')
        cor = request.POST.get('cor')
        Anuncio.objects.create(nome_modelo=modelo, nome_marca=marca, cor=cor)
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

