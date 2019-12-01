#Blog Django

--Crear proyecto y App en Django

1. django-admin startproject django_blog
2. cd django_blog
   2.1 - mkdir templates
   2.2 - cd templates
   2.3 - \$echo "" >> **init**.py
3. mkdir apps
   3.2 - cd apps
   3.3 - \$echo "" >> **init**.py
   3.4 - django-admin startapp blog
4. 'apps.blog', #registramos el app en settings.py INSTALLED_APPS

5. apps/blog/models.py --> Creación la base de datos en el modelo
6. apps/blog/admin.py --> Mostramos los campos del modelo en el admin de Django
7.

** Librerias usadas: 1. Import-export: permite importar datos y exportar 2. ckeditor: Permite crear un campo con herramientas tipo word
** django-admin flush --> borra los datos y reaplica todo
\*\* django-admin flush -- fake (hace migraciones falsas para encontrar el problema)
