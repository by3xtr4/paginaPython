from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('', views.inicio), #esta era nuestra primer view
    path('inicio', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"), #vista mejorada, 
    path('usuarios', views.usuarios, name="Usuarios"),
    path('productos', views.productos, name="Productos"),
    path('newsletter', views.newsletter, name="Newsletter"),
    path('cursoFormulario', views.cursoFormulario, name="cursoFormulario"),
    path('usuarioFormulario', views.usuarioFormulario, name="UsuarioFormulario"),
    path('productosFormulario', views.productosFormulario, name="productosFormulario"),
]

