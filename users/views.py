from django.shortcuts import render
from rest_framework import viewsets
from .models import Livro, Autor
from .serializers import AutorSerializers,LivroSerializers

class LivroViewsSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers

class AutorViewsSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers
#Exemplo view:
#class GeneroLiterarioViewSet(ModelViewSet):
#   queryset = GeneroLiterario.objects.all()
#  serializer_class = GeneroLiterarioSerializer
 