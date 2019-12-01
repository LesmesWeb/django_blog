from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre'] #añado la barra de busqueda (pero no hay acciones)
    list_display = ('nombre','estado','fecha_creacion',) #lista de atributos visibles en el admin

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']
    list_display = ('nombres','coreo','estado','fecha_creación',)

# Register your models here.
admin.site.register(Categoria,CategoriaAdmin) # Heredo de la clase CategoriaAdmin
admin.site.register(Autor,AutorAdmin)