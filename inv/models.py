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
        super(Categoria, self)

    class Meta:
        verbose_name_plural= "Categorias"