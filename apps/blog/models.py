from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria', max_length=100,null=False,blank=False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada',default=True)
    #auto_now = True actualiza el campo cada vez que se actualice el modelo, auto_now_add = True añadirlo solo una vez
    fecha_creacion = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
   

    class Meta:
        verbose_name = 'Categoria' #manera que vamos a indeficar el modelo en el admin
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres de Autor', max_length=255,blank=False,null=False)
    apellidos = models.CharField('Apellidos de Autor', max_length=255,blank=False,null=False)
    facebook = models.URLField('Facebook',null=True,blank=True)
    twitter = models.URLField('Twitter',null=True,blank=True)
    instagram = models.URLField('Instagram',null=True,blank=True)
    web = models.URLField('Web',null=True,blank=True)
    coreo = models.EmailField('Correo Electronico',blank=False,null=False)
    estado = models.BooleanField('Autor Activo/No Activo',default=True)
    #auto_now = True actualiza el campo cada vez que se actualice el modelo, auto_now_add = True añadirlo solo una vez
    fecha_creación = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format({self.apellidos,self.nombres})
    