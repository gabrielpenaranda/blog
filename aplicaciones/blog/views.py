from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.

def home(request):
    posts = Post.objects.filter(estado=True)
    return render(request,'index.djhtml', {'posts': posts})

def generales(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre="Generales"))
    return render(request, 'generales.djhtml', {'posts': posts})
    
def programacion(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre="Programación"))
    return render(request, 'programacion.djhtml', {'posts': posts})

def tecnologia(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre="Tecnología"))
    return render(request, 'tecnologia.djhtml', {'posts': posts})

def videojuegos(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre="Videojuegos"))
    return render(request, 'videojuegos.djhtml', {'posts': posts})

def tutoriales(request):
    posts = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre="Tutoriales"))
    return render(request, 'tutoriales.djhtml', {'posts': posts})