from django.contrib import admin
from .models import Definiciones, Documentos, Normatividad, Eventos

admin.site.register(Definiciones)
admin.site.register(Documentos)
admin.site.register(Normatividad)
admin.site.register(Eventos)

