from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipos(models.Model):
    IdEquipo = models.AutoField(primary_key=True)
    IdUsuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Tipo = models.CharField(max_length=30, null=False)
    Modelo = models.CharField(max_length=30, null=False)
    Marca = models.CharField(max_length=30, null=False)

    def getIdEquipo(self):
        return self.IdEquipo
    

class Reserva(models.Model):
    IdReserva = models.AutoField(primary_key=True)
    IdEquipo = models.ForeignKey(Equipos, on_delete=models.CASCADE, null=False)
    IdUsuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Detalle = models.CharField(max_length=100, null=True)
    FechaInicio = models.DateTimeField(null=False)
    FechaFinal = models.DateTimeField(null=True)

    def getIdEquipo(self):
        return self.IdEquipo
    

class Soportes(models.Model):
    IdSoporte = models.AutoField(primary_key=True)
    IdEquipo = models.ForeignKey(Equipos, on_delete=models.CASCADE, null=False)
    IdUsuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Detalle = models.CharField(max_length=100, null=True)
    FechaInicio = models.DateTimeField(null=False)
    FechaFinal = models.DateTimeField(null=True)