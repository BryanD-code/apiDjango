from rest_framework import serializers
from .models import Proyect, Suma, Alergias, Tipo


#datos a ser consultados 

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        #fields = '__all__'
        read_only_fields = ('created_at',)#campos solo modo lectura
        #view set para decidir quien puede consultar esto 
class SumaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suma
        fields = ('id', 'tipo_id', 'Platos', 'Imagenes', 'Precio', 'Alergia', 'created_at')
        read_only_fields = ('created_at',)

class AlergiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergias
        fields = ('id', 'ImagenAler', 'Informacion')
        read_only_fields = ('id',)
class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'TipoEspecifico')
        read_only_fields = ('id',)

