from rest_framework import serializers
from licao.models import Licao

class LicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licao
        fields = ['id', 'titulo', 'conteudo_html']
    
    def create(self, validated_data):
        
        licao = Licao.objects.create(**validated_data)
        return licao
        
class LicaoHtmlUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Licao
        fields = ['conteudo_html']
        
    def validate_conteudo_html(self, value):
        licao = self.instance
        if licao and licao.conteudo_html == value:
            raise serializers.ValidationError('O novo conteúdo HTML deve ser diferente do atual')
        return value
    

    