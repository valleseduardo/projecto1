from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email} "

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email} Profesion: {self.profesion}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} Camada: {self.camada}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return self.nombre