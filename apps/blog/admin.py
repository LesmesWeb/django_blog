from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Import export Categoria
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre'] #añado la barra de busqueda
    list_display = ('nombre','estado','fecha_creacion',) #lista de atributos visibles en el admin
    resource_class = CategoriaResource

# Import export Autor
class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres','apellidos']
    list_display = ('nombres','apellidos','correo','estado','fecha_creación',)
    resource_class = AutorResource

# Import export Post
class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','autor']
    list_display = ('titulo','descripcion','autor','categoria','estado',)
    resource_class = PostResource


# Register your models here.
admin.site.register(Categoria,CategoriaAdmin) # Heredo de la clase CategoriaAdmin
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)