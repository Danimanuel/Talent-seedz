from res_framework import serializers
from models import Livro

class LivroSerializers(serializers.serializer):
    class Meta:
        model = Livro
        fields = '__all__'