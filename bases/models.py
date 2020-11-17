from django.db import models
from django.contrib.auth.models import User

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True) #'default' para que cada vez que se agreguen datos por default sea verdadero el campo.
    fc = models.DateTimeField(auto_now_add=True) #'auto_now_add' para que solo se actualice la fecha cuando se agregue el campo.
    fm = models.DateTimeField(auto_now=True) #'auto_now' para que siempre que pase algo con el registro se actualice la fecha.
    uc = models.ForeignKey(User, on_delete=models.CASCADE) #Conexión con la user que ya tiene django por default.
    um = models.IntegerField(blank=True,null=True) #No se pueden tener dos ForeignKey, por lo tanto sera tipo entero y puede quedar en blanco.

    class Meta:
        abstract= True #Para que a la hora de hacer migraciones, no tome encuenta esta clase.

