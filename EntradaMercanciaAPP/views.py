from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import EntradaMercancia, Proveedor, EntradaMercanciaProducto,Producto
from django.core import serializers
from django.views import generic

    
def index(request):
    entradas = EntradaMercancia.objects.all()
    #template = loader.get_template('EntradaMercancia/index.html')
    context = {'entradas': entradas,}
    #json = serializers.serialize('json', context)
    return render(request,'EntradaMercancia/index.html',context,)

    #return HttpResponse(json, content_type='application/json')      
        
def create(request):
    print ('===Metodo Crear Entrada de Mercancia=====')
    listaProveedores = Proveedor.objects.all()
    listaProductos = Producto.objects.all()
    listaProductosCarrito = [EntradaMercanciaProducto]
    template = loader.get_template('EntradaMercancia/create.html')
    context = {
        'listaProveedores': listaProveedores,
        'listaProductos': listaProductos,
        'listaProductosCarrito': listaProductosCarrito,
    }
    return render(request,'EntradaMercancia/create.html',context,)
    
    
class BookListView(generic.ListView):
    model = EntradaMercanciaProducto