from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoriaFK = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
        
        
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre 

class StatusCatalogo(models.Model):
    #id creado automaticamente
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre 
        
        
class Status(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    idStatusCatalogoFk = models.ForeignKey(StatusCatalogo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre        
defaultIDSTATUS =1            
class EntradaMercancia(models.Model):
    #id se crea automaticamente
    folio = models.IntegerField(default=1)
    remision = models.CharField(max_length=30)
    fecha  = models.DateTimeField('Fecha de Ingreso')
    idProveedorFk = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    idStatusFk = models.ForeignKey(Status, on_delete=models.CASCADE, default = defaultIDSTATUS)
    comentarios = models.CharField(max_length=200)
    idUsuarioFk = models.ForeignKey(User, on_delete=models.CASCADE)
    costoTotal = models.FloatField()
    cantidadTotal =models.IntegerField()

    def __str__(self):
        return self.remision
 
class EntradaMercanciaProducto(models.Model):
    #id se crea automaticamente
    idEMFk = models.ForeignKey(EntradaMercancia, on_delete=models.CASCADE)
    idProductoFk = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idStatusFk = models.ForeignKey(Status, on_delete=models.CASCADE, default = defaultIDSTATUS)
    costo = models.FloatField()
    cantidad =models.IntegerField()
    comentarios = models.CharField(max_length=200)
    def __str__(self):
        return self.comentarios
        
class Bodega(models.Model):
    #id creado automaticamente
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre         
        
class Existencia(models.Model):
    #id se crea automaticamente
    idProductoFk = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idStatusFk = models.ForeignKey(Status, on_delete=models.CASCADE)
    idBodegaFk = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    cantidad =models.IntegerField()
    def __str__(self):
        return self.idProductoFk    
        
class UnidadVenta(models.Model):
    #id creado automaticamente
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    cantidad =models.IntegerField() 
    def __str__(self):
        return self.nombre  
        
        
class Cliente(models.Model):
    #id creado automaticamente
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre  
        
class MantenimientoPrecios(models.Model):
    #id creado automaticamente
    idProductoFk = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idClienteFk = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idUnidadVentaFk = models.ForeignKey(UnidadVenta, on_delete=models.CASCADE)
    precioVenta = models.FloatField()
    def __str__(self):
        return self.idProductoFk
        
class AjusteMercancia(models.Model):
    #id creado automaticamente
    idExistenciaProductoFk = models.ForeignKey(Existencia, on_delete=models.CASCADE)
    cantidadAnterior = models.IntegerField() 
    cantidadNueva = models.IntegerField() 
    idUsuarioFk = models.ForeignKey(User, on_delete=models.CASCADE)
    comentarios = models.CharField(max_length=200)
    
class Venta(models.Model):
    #id se crea automaticamente
    folio = models.IntegerField(default=1)
    fecha  = models.DateTimeField('Fecha de Ingreso')
    idClienteFk = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idStatusFk = models.ForeignKey(Status, on_delete=models.CASCADE, default = defaultIDSTATUS)
    comentarios = models.CharField(max_length=200)
    idUsuarioFk = models.ForeignKey(User, on_delete=models.CASCADE)
    precioTotal = models.FloatField()
    cantidadTotal =models.IntegerField()

    def __str__(self):
        return self.remision
 
class VentaProducto(models.Model):
    #id se crea automaticamente
    idVFk = models.ForeignKey(Venta, on_delete=models.CASCADE)
    idProductoFk = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idUnidadVentaFk = models.ForeignKey(UnidadVenta, on_delete=models.CASCADE)
    idStatusFk = models.ForeignKey(Status, on_delete=models.CASCADE)
    precioVenta = models.FloatField()
    cantidad =models.IntegerField()
    comentarios = models.CharField(max_length=200)
    def __str__(self):
        return self.comentarios    
        
class CatalogoOperaciones(models.Model):
    #id creado automaticamente
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre  
        
class Operaciones(models.Model):
    #id creado automaticamente
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    idCatalogoFk = models.ForeignKey(CatalogoOperaciones, on_delete=models.CASCADE)
    entrada_salida = models.BooleanField()
    def __str__(self):
        return self.nombre          
        
class CorteCaja(models.Model):
    #id creado automaticamente
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    idUsuarioFk = models.ForeignKey(User, on_delete=models.CASCADE)
    entrada_salida = models.BooleanField()
    saldoAnterior = models.FloatField()
    saldoNuevo = models.FloatField()
    idStatusFk = models.ForeignKey(Status, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre  
        
class Movimientos(models.Model):
    #id creado automaticamente
    idOperacionesFk = models.ForeignKey(CatalogoOperaciones, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    comentarios = models.CharField(max_length=200)
    idCorteFk = models.ForeignKey(CorteCaja, on_delete=models.CASCADE)
    idUsuarioFk = models.ForeignKey(User, on_delete=models.CASCADE)
    entrada_salida = models.BooleanField()
    idStatusFk = models.ForeignKey(Status, on_delete=models.CASCADE)
    def __str__(self):
        return self.idOperacionesFk   
        
        
        
        
        
        
        
        