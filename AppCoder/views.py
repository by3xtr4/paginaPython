from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso


# def curso(request):
#       curso =  Curso(nombre="Desarrollo web", camada="19881")
#       curso.save() 
#       curso2 = Curso(nombre="Desarrollo Back", camada="222222")     
#       curso2.save()     
#       documentoDeTexto = f"El Curso 1 es: {curso.nombre}   Camada: {curso.camada}, el curso 2 es: {curso2.nombre} Camada: {curso2.camada} "
#       return HttpResponse(documentoDeTexto)

#estas son mis url, diferentes vistas.

def inicio(request):
      return render(request, "AppCoder/inicio.html")

def cursos(request):
      return render(request, "AppCoder/cursos.html")

def profesores(request):
      return render(request, "AppCoder/profesores.html")


def estudiantes(request):
      return render(request, "AppCoder/estudiantes.html")


def entregables(request):
      return render(request, "AppCoder/entregables.html")

#nuevaVista, mia
def contador(request):
      return render(request, "AppCoder/contador.html")