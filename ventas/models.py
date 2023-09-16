from django.db import models

# Create your models here.
class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()
    comuna = models.CharField(max_length=50) 
    ciudad = models.CharField(max_length=50)

class Proveedor(models.Model):
    codigo = models.CharField(max_length=20,unique=True)
    nombre = models.CharField(max_length=50)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=9)
    pagina_web = models.URLField()

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Producto(models.Model):
    identificador = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Telefono(models.Model):
    numero = models.CharField(max_length=9)

class Cliente(models.Model):
    codigo = models.CharField(max_length=8,unique=True)
    nombre = models.CharField(max_length=50)
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE)
    telefonos = models.ManyToManyField(Telefono)


class Venta(models.Model):
    nro_factura = models.CharField(max_length=20,unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=5,decimal_places=2)
    monto_final = models.DecimalField(max_digits=5,decimal_places=2)
    productos = models.ManyToManyField(Producto)

class ItemVendido(models.Model):
    venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=5,decimal_places=5)
    cantidad = models.PositiveIntegerField()
    monto_total = models.DecimalField(max_digits=5,decimal_places=2)