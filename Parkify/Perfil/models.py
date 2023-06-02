# Importaciones necesarias
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404
from django import forms


class Usuario(AbstractUser):
    # Los atributos ya están predeterminados en el usuario abstracto de Django
    usuario_ptr = models.IntegerField(primary_key=True, default=0)
    password = models.CharField(max_length=128, default='0000')
    username = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios')


class Portero(Usuario):
    # Atributos
    usuarioEmpresaVig = models.CharField(max_length=50)


class AdminEAFIT(Usuario):
    # Atributos
    id = models.IntegerField(primary_key= True, default=0)
    cuentaAdmin = models.CharField(max_length=50)


class AdminPARKIFY(Usuario):
    # Atributos
    id = models.IntegerField(primary_key=True, default=0)
    cuentaAdmin = models.CharField(max_length=50)


class Evento(models.Model):
    # Atributos
    idEvento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    organizador = models.CharField(max_length=100)

class Vehiculo(models.Model):
    # Atributos
    idVehiculo = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=50)
    tipoVehiculo = models.CharField(max_length=10)
    combustible = models.CharField(max_length=10)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class VehiculoForm(forms.Form):
    # Atributos
    modelo = forms.CharField(label='Modelo', max_length=50)
    tipo_vehiculo_choices = [('moto', 'Moto'), ('carro', 'Carro')]
    tipo_vehiculo = forms.ChoiceField(choices=tipo_vehiculo_choices, label='Tipo de Vehículo')
    combustible_choices = [('eléctrico', 'Eléctrico'), ('gasolina', 'Gasolina'), ('hibrido', 'Híbrido'), ('otros', 'Otros')]
    combustible = forms.ChoiceField(choices=combustible_choices, label='Combustible')


