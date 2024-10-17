from rest_framework import serializers
from conta.models import Usuario
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UsuarioCreateSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email','senha',  'data_nascimento']
        extra_kwargs = {
            'senha': {'write_only': True}
        }
        
    def validate_senha(self,value):
        if len(value) < 8:
            raise serializers.ValidationError('A senha deve ter no mínimo 8 caracteres')
        return value    
        
    def create(self, validated_data):
        senha = validated_data.pop('senha')
        usuario = Usuario.objects.create(**validated_data)
        usuario.set_password(senha)
        usuario.save()
        return usuario
    
class UsuarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'data_nascimento']
        
# class UsuarioUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ['id', 'nome', 'email', 'data_nascimento']
#         read_only_fields = ['email']
        
#     def update(self, instance, validated_data):
#         instance.nome = validated_data.get('nome', instance.nome)
#         instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)
#         instance.save()
#         return instance
    
        
