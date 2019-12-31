from django.shortcuts import render
from .models import Post,Categoria
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Q
#Paginación
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True)

    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |  #FILTRO POR O
            Q(descripcion__icontains = queryset) #icontains no importa si hay mayusculas o minusculas
        ).distinct()#distinct trae los que no son iguales

    #Paginator recibe dos parametros el primero es la lista (Post), y la paginación
    paginator = Paginator(posts,2)
    #obtiene la pagina en la cuestión actual
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    return render(request,'index.html',{'posts':posts})

def detallePost(request,slug):
    #Validación de 404 manera agil
    post = get_object_or_404(Post,slug=slug)
    return render(request,'post.html',{'detalle_post':post})

def generales(request):
    #validación mas detallada
    
    try:
        queryset = request.GET.get("buscar")
        posts = Post.objects.filter(
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='general') #__exact especifica que el campo debe ser identico
        )

        if queryset:
            posts=Post.objects.filter(
                Q(titulo__icontains = queryset) |  #FILTRO POR O
                Q(descripcion__icontains = queryset), #icontains no importa si hay mayusculas o minusculas
                estado=True,
                categoria=Categoria.objects.get(nombre__iexact='general'),

        ).distinct()#distinct trae los que no son iguales
    except Post.DoesNotExist:
        raise Http404("No existe la Post correcto")

    except Categoria.DoesNotExist:
        raise Http404("No existe la Categoria correcto")

    return render(request,'generales.html',{'posts':posts}) 

def programacion(request):
    try:
        queryset = request.GET.get("buscar")
        posts = Post.objects.filter(
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Programación') #__exact especifica que el campo debe ser identico
        )

        if queryset:
            posts=Post.objects.filter(
                Q(titulo__icontains = queryset) |  #FILTRO POR O
                Q(descripcion__icontains = queryset), #icontains no importa si hay mayusculas o minusculas
                estado=True,
                categoria=Categoria.objects.get(nombre__iexact='Programación'),

        ).distinct()#distinct trae los que no son iguales
    except Post.DoesNotExist:
        raise Http404("No existe la Post correcto")

    except Categoria.DoesNotExist:
        raise Http404("No existe la Categoria correcto")

    return render(request,'programacion.html',{'posts':posts})

def tutoriales(request):
    try:
        queryset = request.GET.get("buscar")
        posts = Post.objects.filter(
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Tutoriales') #__exact especifica que el campo debe ser identico
        )

        if queryset:
            posts=Post.objects.filter(
                Q(titulo__icontains = queryset) |  #FILTRO POR O
                Q(descripcion__icontains = queryset), #icontains no importa si hay mayusculas o minusculas
                estado=True,
                categoria=Categoria.objects.get(nombre__iexact='Tutoriales'),

        ).distinct()#distinct trae los que no son iguales
    except Post.DoesNotExist:
        raise Http404("No existe la Post Tutoriales correcto")

    except Categoria.DoesNotExist:
        raise Http404("No existe la Categoria Tutoriales correcto")

    return render(request,'tutoriales.html',{'posts':posts})

def tecnologia(request):
    try:
        queryset = request.GET.get("buscar")
        posts = Post.objects.filter(
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Tecnología') #__exact especifica que el campo debe ser identico
        )

        if queryset:
            posts=Post.objects.filter(
                Q(titulo__icontains = queryset) |  #FILTRO POR O
                Q(descripcion__icontains = queryset), #icontains no importa si hay mayusculas o minusculas
                estado=True,
                categoria=Categoria.objects.get(nombre__iexact='Tecnología'),

        ).distinct()#distinct trae los que no son iguales
    except Post.DoesNotExist:
        raise Http404("No existe la Post Tutoriales correcto")

    except Categoria.DoesNotExist:
        raise Http404("No existe la Categoria Tutoriales correcto")

    return render(request,'tecnologia.html',{'posts':posts})

def videojuegos(request):
    try:
        queryset = request.GET.get("buscar")
        posts = Post.objects.filter(
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Videojuegos') #__exact especifica que el campo debe ser identico
        )

        if queryset:
            posts=Post.objects.filter(
                Q(titulo__icontains = queryset) |  #FILTRO POR O
                Q(descripcion__icontains = queryset), #icontains no importa si hay mayusculas o minusculas
                estado=True,
                categoria=Categoria.objects.get(nombre__iexact='Videojuegos'),

        ).distinct()#distinct trae los que no son iguales
    except Post.DoesNotExist:
        raise Http404("No existe la Post Tutoriales correcto")

    except Categoria.DoesNotExist:
        raise Http404("No existe la Categoria Tutoriales correcto")

    return render(request,'videojuegos.html',{'posts':posts})