from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Obtiene el ultimo id de un usuario registrado. Sirve para linkear de usuario a cliente (Todo usuario que se loguea es un cliente)
def get_last_user_id():
    last_user = User.objects.last()
    if last_user:
        return last_user.id
    else:
        return 1  #al else no entra 

class Cliente(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=1  # Utiliza el método como valor predeterminado
    )
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.apellido} {self.nombre}"

class Mesa(models.Model):
    ocupado = models.BooleanField(default=False)
    descripcion = models.TextField(null=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"Mesa: {self.id}"



