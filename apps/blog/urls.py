from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='index'),
    path('<slug:slug>/',detallePost, name='detalle_post'),
    path('generales/',generales,name='generales'),
    path('programacion/',programacion,name='programacion'),
    path('tutoriales/',tutoriales,name='tutoriales'),
    path('tecnologia/',tecnologia,name='tecnologia'),
    path('videojuegos/',videojuegos,name='videojuegos'),
]
