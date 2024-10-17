from rest_framework import generics,status, permissions
from rest_framework.response import Response 
from rest_framework_simplejwt.tokens import RefreshToken
from conta.serializer import (
    UsuarioCreateSerializer,
    UsuarioDetailSerializer,

)
from conta.models import Usuario

from conta.permission import IsOwnerOrReadOnly

class UsuarioCreateView(generics.CreateAPIView):
    serializer_class = UsuarioCreateSerializer
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]



class UsuarioLoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        senha = request.data.get('senha')
        
        
        usuario = Usuario.objects.filter(email=email).first()
        print(usuario)
        
        if usuario is None:
            return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        if not usuario.check_password(senha):
            return Response({'error': 'Senha incorreta'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        refresh = RefreshToken.for_user(usuario)
        return Response({
            "token": str(refresh.access_token),
            "refresh": str(refresh)
        })