from rest_framework import serializers
from .models import Proyect, Suma, Alergias, Tipo

# DATOS A SER CONSULTADOS

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)

class AlergiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergias
        # Aseguramos traer todos los campos necesarios
        fields = ('id', 'ImagenAler', 'Informacion')
        read_only_fields = ('id',)

class SumaSerializer(serializers.ModelSerializer):
    # CAMBIO IMPORTANTE:
    # Definimos 'alergias_ids' para que extraiga solo los IDs de la relación ManyToMany 'alergias'
    alergias_ids = serializers.PrimaryKeyRelatedField(
        many=True, 
        read_only=True, 
        source='alergias'
    )

    class Meta:
        model = Suma
        # Quitamos 'Alergia' (texto antiguo) y ponemos 'alergias_ids' (array nuevo)
        fields = ('id', 'tipo_id', 'Platos', 'Imagenes', 'Precio', 'alergias_ids', 'created_at')
        read_only_fields = ('created_at',)

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'TipoEspecifico')
        read_only_fields = ('id',)