from rest_framework import serializers
from models import Licao

class LicaoSerializer(serializers.Serializer):
    class Meta:
        
        model = Licao
        fields = ['id', 'titulo', 'conteudo_html']
        