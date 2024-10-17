from django.db import models

# Create your models here.
class Contacto(models.Model):
    no = models.IntegerField(null=True, blank=True, unique=True)
    grado = models.CharField(max_length=100)
    nom_ape  = models.CharField(max_length=100)
    fuerza = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)
    cargo_actual = models.CharField(max_length=100)
    tel_oficina = models.CharField(max_length=100)
    tel_ip = models.CharField(max_length=100)
    tel_celular = models.CharField(max_length=100)
    correo_inst = models.CharField(max_length=100)
    correo_personal = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.grado} {self.nombre} {self.apellido} - {self.cargo_actual}"