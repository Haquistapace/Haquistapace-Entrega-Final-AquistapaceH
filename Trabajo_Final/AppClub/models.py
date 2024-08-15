from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=40)
    dia = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='deportes/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Socio(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)


