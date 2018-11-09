from django.db import models

# Create your models here.

class Ponente(models.Model):
    nombre = models.CharField(
        max_length = 100
    )

    trabajo = models.CharField(
        max_length = 100,
        blank = True
    )

    foto = models.URLField(
        max_length = 400,
        blank = True
    )

    prioridad = models.IntegerField(
        default = 0
    ) 

    def __str__(self):
        return self.nombre

class Charla(models.Model):

    titulo = models.CharField(
        max_length = 100
    )

    descripcion = models.TextField(
        max_length = 255
    )

    ponentes = models.ManyToManyField(
        Ponente
    )

    fecha = models.DateField()
    
    hora = models.TimeField()

    lugar = models.CharField(
        max_length = 150
    )

    def __str__(self):
        return selt.titulo