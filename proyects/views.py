from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import SumaSerializer, TipoSerializer,AlergiaSerializer
from .models import Suma, Tipo, Alergias



class SumaViewSet(viewsets.ModelViewSet):
    queryset = Suma.objects.all().order_by('id')
    serializer_class = SumaSerializer

    # Fíjate que esta línea tiene sangría (espacio a la izquierda)
    def create(self, request, *args, **kwargs):
        # Este print saldrá en tu terminal si el código se está ejecutando bien
        print("--> INTENTANDO CREAR LISTA DE PLATOS...") 

        # Si request.data es una lista, usamos many=True
        es_una_lista = isinstance(request.data, list)
        
        serializer = self.get_serializer(data=request.data, many=es_una_lista)
        
        # Validamos y guardamos
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all().order_by('id')
    serializer_class = TipoSerializer

class AlergiasViewSet(viewsets.ModelViewSet):
    queryset = Alergias.objects.all().order_by('id')
    serializer_class = AlergiaSerializer