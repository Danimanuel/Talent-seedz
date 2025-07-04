from rest_framework import serializers
from .models import Livro, Autor


class LivroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'


class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Autor
        fields = '__all__'
    