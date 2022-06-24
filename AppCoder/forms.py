from django import forms #consumo libreria de forms de django. Ojo con tipeo, es exacto

class CursoFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(max_length=40)
    camada = forms.CharField(max_length=40)

class UsuarioFormulario(forms.Form):
    #Especifico los campos
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    user= forms.CharField(max_length=30)
    contra= forms.CharField(max_length=30)
    email= forms.EmailField()

class ProductosFormulario(forms.Form):
    #Especifico los campos
    nombre= forms.CharField(max_length=30)
    tipo= forms.CharField(max_length=30)
    estado = forms.BooleanField()