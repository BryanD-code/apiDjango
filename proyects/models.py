from django.db import models

# 1. MOVER ESTA CLASE ARRIBA (Antes de Suma)
class Alergias(models.Model):
    # Sugerencia: URLField es mejor para imagenes, pero CharField funciona
    ImagenAler = models.CharField(max_length=500) 
    Informacion = models.CharField(max_length=500)  
    
    def __str__(self):
        return self.Informacion

class Proyect(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Tipo(models.Model):
    TipoEspecifico = models.CharField(max_length=200)
    
    def __str__(self):
        return self.TipoEspecifico

class Suma(models.Model):
    tipo_id = models.CharField(max_length=200)
    Platos = models.CharField(max_length=200)
    Imagenes = models.CharField(max_length=500)
    Precio = models.CharField(max_length=200)
    
    # 2. CAMBIO AQUÍ: Quitamos el campo de texto antiguo y ponemos la relación
    # Esto permite que un plato tenga muchas alergias [1, 5, 8]
    alergias = models.ManyToManyField(Alergias, related_name='platos', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Platos