from django.db import models

# Creo los modelos

class Newsletter(models.Model):
    nombre=models.CharField(max_length=40)
    email = models.EmailField()

class Usuarios(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    user= models.CharField(max_length=30)
    contra= models.CharField(max_length=30)
    email= models.EmailField()

class Productos(models.Model):
    nombre= models.CharField(max_length=30)
    tipo= models.CharField(max_length=30)
    estado = models.BooleanField()

class Cursos(models.Model):
    nombre= models.CharField(max_length=30)
    camada = models.CharField(max_length=30)