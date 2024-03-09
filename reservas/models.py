from django.db import models

# Create your models here.
class Mesa(models.Model):
    pass

class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    correo = models.EmailField()
    mesa = models.ForeignKey(
        Mesa,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

class Estado(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    ocupado = models.BooleanField(default=False)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def esta_ocupada(self, fecha):
        return self.fecha_inicio <= fecha <= self.fecha_fin

