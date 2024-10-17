from rest_framework import generics, status
from licao.serializer import LicaoSerializer, LicaoHtmlUpdateSerializer
from licao.models import Licao
from rest_framework.response import Response

class LicaoCreateView(generics.CreateAPIView):
    serializer_class = LicaoSerializer
    queryset = Licao.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        
class LicaoUpdateHtmlView(generics.UpdateAPIView):
    serializer_class = LicaoHtmlUpdateSerializer
    queryset = Licao.objects.all()
    
        
        
class LicaoListView(generics.ListAPIView):
    serializer_class = LicaoSerializer
    queryset = Licao.objects.all()
    
    
class LicaoDetailView(generics.RetrieveAPIView):
    serializer_class = LicaoSerializer
    queryset = Licao.objects.all()

class LicaoDeleteView(generics.DestroyAPIView):
    serializer_class = LicaoSerializer
    queryset = Licao.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

