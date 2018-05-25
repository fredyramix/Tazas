from django.contrib import admin

from .models import Categoria, Producto, EntradaMercancia,Proveedor,EntradaMercanciaProducto,Bodega,Existencia,StatusCatalogo,Status

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(EntradaMercancia)
admin.site.register(EntradaMercanciaProducto)

admin.site.register(Bodega)
admin.site.register(Existencia)
admin.site.register(Status)
admin.site.register(StatusCatalogo)
