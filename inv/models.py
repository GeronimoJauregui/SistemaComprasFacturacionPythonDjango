from django.db import models
from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripción de la categoria",
        unique=True
    )
    def __str__(self):
        return '{}'.format(self.descripcion) #Convertir el la descripcion a texto entendible

    def save(self):
        self.descripcion = self.descripcion.upper() #Guardar la descripcion en mayusculas
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural= "Categorias"

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) #Conexion con categoria.
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripción de la categoria",
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() #Guardar la descripcion en mayusculas
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural= "Sub categorias"
        unique_together = ('categoria','descripcion') #Para que no se puedan repetir sub categorias en una misma categoria.

class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripción de la marca",
        unique=True
    )
    def __str__(self):
        return '{}'.format(self.descripcion) #Convertir el la descripcion a texto entendible
    
    def save(self):
        self.descripcion = self.descripcion.upper() #Guardar la descripcion en mayusculas
        super(Marca, self).save()

    class Meta:
        verbose_name_plural= "Marcas"

class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text="Descripción de la Unidad Medida",
        unique=True
    )
    def __str__(self):
        return '{}'.format(self.descripcion) #Convertir el la descripcion a texto entendible
    
    def save(self):
        self.descripcion = self.descripcion.upper() #Guardar la descripcion en mayusculas
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural= "Unidades de medida"

class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateTimeField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.descripcion) #Convertir el la descripcion a texto entendible
    
    def save(self):
        self.descripcion = self.descripcion.upper() #Guardar la descripcion en mayusculas
        super(Producto, self).save()

    class Meta:
        verbose_name_plural= "Productos"
        unique_together = ('codigo','codigo_barra')