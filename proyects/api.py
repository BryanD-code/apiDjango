# ARCHIVO: [tu_app]/api.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProyectSerializer, SumaSerializer, TipoSerializer, AlergiaSerializer
from .models import Proyect, Suma, Tipo, Alergias
from rest_framework import permissions

# --- LÓGICA BASE PARA CREACIÓN MASIVA ---
def bulk_create_mixin(viewset_instance, request, *args, **kwargs):
    """Método reutilizable para manejar la creación individual o masiva."""
    print(f"--> EJECUTANDO CREACIÓN MASIVA/INDIVIDUAL para: {viewset_instance.__class__.__name__}")
    
    # 1. Detectar si la data entrante es una lista (True para creación masiva)
    es_una_lista = isinstance(request.data, list)
    
    # 2. Inicializar el serializador, pasando many=True si es una lista
    serializer = viewset_instance.get_serializer(data=request.data, many=es_una_lista)
    
    # 3. Validar y guardar
    serializer.is_valid(raise_exception=True)
    viewset_instance.perform_create(serializer)
    
    # 4. Retornar la respuesta exitosa
    headers = viewset_instance.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# -----------------------------------------------------------------
# VIEWSETS CON CREACIÓN MASIVA HABILITADA
# -----------------------------------------------------------------

class ProyectViewSet(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()
    serializer_class = ProyectSerializer
    
# --- VIEWSET SUMA (PLATO) ---
class SumaViewSet(viewsets.ModelViewSet):
    queryset = Suma.objects.all().order_by('id')
    serializer_class = SumaSerializer

    # CREACIÓN MASIVA HABILITADA
    def create(self, request, *args, **kwargs):
        return bulk_create_mixin(self, request, *args, **kwargs)
    
# --- VIEWSET TIPO ---
class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

    # CREACIÓN MASIVA HABILITADA
    def create(self, request, *args, **kwargs):
        return bulk_create_mixin(self, request, *args, **kwargs)
        
 
# --- VIEWSET ALERGIAS ---
class AlergiasViewSet(viewsets.ModelViewSet):
    queryset = Alergias.objects.all()
    serializer_class = AlergiaSerializer 
    
    # CREACIÓN MASIVA HABILITADA
    def create(self, request, *args, **kwargs):
        return bulk_create_mixin(self, request, *args, **kwargs)