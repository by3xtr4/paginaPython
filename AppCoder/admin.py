from django.contrib import admin #traigo esta dependencia, para habilitar el admin
from .models import* #importo models

#registro los modelos en el admin, modelos que ya cree.
#RENOMBRO
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)