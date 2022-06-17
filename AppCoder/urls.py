from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('', views.inicio), #esta era nuestra primer view
    path('inicio', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"), #vista mejorada, 
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entreganbles"),
    path('contador', views.contador, name="contador"),
]

