from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Cursos, Usuarios, Productos, Newsletter
from AppCoder.forms import CursoFormulario, UsuarioFormulario, ProductosFormulario

#estas son mis url, diferentes vistas.
def inicio(request): #vista inicio
      return render(request, "AppCoder/inicio.html")

def cursos(request): #vista cursos
      return render(request, "AppCoder/cursos.html")

def usuarios(request):#vista usuarios
      return render(request, "AppCoder/usuarios.html")


#curso,
def cursoFormulario(request):#vista usuarios, la edito para que guarde
      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  print(miFormulario)

                  informacion = miFormulario.cleaned_data
                  defino_curso = Cursos (nombre=informacion['nombre'], camada=informacion['camada']) 
                  defino_curso.save()
                  return render(request, "AppCoder/curso_registrado.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/cursoformulario.html", {"miFormulario":miFormulario})


#usuarios,
def usuarioFormulario(request):#vista usuarios, la edito para que guarde
      if request.method == 'POST':

            miFormulario = UsuarioFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  print(miFormulario)

                  informacion = miFormulario.cleaned_data
                  guardo_usuario = Usuarios (nombre=informacion['nombre'], apellido=informacion['apellido'], user=informacion['user'], contra=informacion['contra'], email=informacion['email']) 
                  guardo_usuario.save()
                  return render(request, "AppCoder/usuario_registrado.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= UsuarioFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/usuarioformulario.html", {"miFormulario":miFormulario})



#productos, ojo con el print!

#usuarios,
def productosFormulario(request):#vista usuarios, la edito para que guarde
      if request.method == 'POST':

            miFormulario = ProductosFormulario(request.POST) #aquí mellega toda la información del html - sale de models

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  print(miFormulario)

                  informacion = miFormulario.cleaned_data
                  guardo_producto = Productos (nombre=informacion['nombre'], tipo=informacion['tipo'], estado=informacion['estado']) 
                  guardo_producto.save()
                  return render(request, "AppCoder/producto_registrado.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProductosFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/productosformulario.html", {"miFormulario":miFormulario})








def productos(request):#vista productos
      return render(request, "AppCoder/productos.html")

def newsletter(request):#vista newsletter
      return render(request, "AppCoder/newsletter.html")
