# from django.db import models


# class Registro(models.Model):
#     nombre = models.CharField(max_length=100)
#     def __str__(self):
#         return self.nombre

from django.db import models

class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.latitud}, {self.longitud})"
