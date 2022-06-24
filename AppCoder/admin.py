from django.contrib import admin #traigo esta dependencia, para habilitar el admin
from .models import* #importo models

#registro los modelos en el admin, modelos que ya cree.
#RENOMBRO
admin.site.register(Cursos)
admin.site.register(Productos)
admin.site.register(Usuarios)
admin.site.register(Newsletter)