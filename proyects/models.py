from django.db import models

# Create your models here.
class Proyect(models.Model):
    title = models.CharField(max_length=200)#de caracteres
    description = models.TextField()#texto extenso 
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)#añade fecha y hora
    
    #
    def __str__(self):
        return self.title
    
class Suma(models.Model):
    tipo_id = models.CharField(max_length=200)
    Platos = models.CharField(max_length=200)
    Imagenes = models.CharField(max_length=500)
    Precio = models.CharField(max_length=200)
    Alergia = models.CharField(max_length=500,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)#añade fecha y hora

    def __str__(self):
        return self.Platos
class Tipo(models.Model):
    TipoEspecifico = models.CharField(max_length=200)
    
    def __str__(self):
        return self.TipoEspecifico
    
class Alergias(models.Model):
    ImagenAler = models.CharField(max_length=500)
    Informacion = models.CharField(max_length=500)  
    
    def __str__(self):
        return self.Informacion