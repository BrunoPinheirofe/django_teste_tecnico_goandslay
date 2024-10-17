from rest_framework import generics
from licao.serializer import LicaoSerializer
from licao.models import Licao

class LicaoCreateView(generics.CreateAPIView):
    serializer_class = LicaoSerializer
    queryset = Licao.objects.all()

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
        
class LicaoEdidView(generics.UpdateAPIView):
    serializer_class = LicaoSerializer
    queryset = Licao.objects.all()

    def perform_update(self, serializer):
        serializer.save(autor=self.request.user)
        
