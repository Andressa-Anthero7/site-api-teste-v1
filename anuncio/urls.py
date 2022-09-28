from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar-anuncio/', views.criar, name='criar-anuncio'),
    path('editar-anuncio/<int:pk>/', views.editar, name='editar-anuncio'),
    path('deletar-anuncio/<int:pk>/', views.deletar, name='deletar-anuncio'),
]
