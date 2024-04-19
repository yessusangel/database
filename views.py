from django.shortcuts import render
from .models import categoriaproductos



# Create your views here.


def listarcategoria(request);
    listadecategorias = categoriaproductos.objects.all()
    return render(request,'listarcategoria.html'{'listar':listadecategorias})

def agregarcategoria(request): 
return render (request,'agregarcategoria.html')



