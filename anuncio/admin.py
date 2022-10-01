from django.contrib import admin
from anuncio.models import Anuncio, Anunciante


class Tabela(admin.ModelAdmin):
    list_display = ('id', 'nome_marca', 'nome_modelo', 'cor')
    list_display_links = ('id', 'nome_marca', 'nome_modelo', 'cor')
    search_fields = ('id', 'nome_marca', 'nome_modelo', 'cor')


admin.site.register(Anuncio, Tabela)
admin.site.register(Anunciante)
