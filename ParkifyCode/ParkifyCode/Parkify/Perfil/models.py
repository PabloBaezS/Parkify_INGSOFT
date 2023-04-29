from django.db import models
from django.http import Http404
from django.shortcuts import get_object_or_404


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    contrasena = models.CharField(max_length=50)

    def login(self, correo, contrasena):
        try:
            usuario = get_object_or_404(Usuario, correo=correo, contrasena=contrasena)
            return True
        except Http404:
            return False

    def registro(self, nombre, correo, contrasena):
        usuario = Usuario(nombre=nombre, correo=correo, contraseña=contrasena)
        usuario.save()
        return usuario


class Vehiculo(models.Model):
    idVehiculo = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=50)
    tipoVehiculo = models.CharField(max_length=10)
    combustible = models.CharField(max_length=10)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Portero(models.Model):
    idPortero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    contrasena = models.CharField(max_length=50)
    usuarioEmpresaVig = models.CharField(max_length=50)

    def login(self, correo, contrasena):
        try:
            usuario = get_object_or_404(Portero, correo=correo, contrasena=contrasena)
            return True
        except Http404:
            return False

    def registro(self, nombre, correo, contrasena):
        portero = Usuario(nombre=nombre, correo=correo, contraseña=contrasena)
        portero.save()
        return portero


class AdminEAFIT(models.Model):
    idAdminEAFIT = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cuentaAdmin = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

    def login(self, correo, contrasena):
        try:
            usuario = get_object_or_404(AdminEAFIT, correo=correo, contrasena=contrasena)
            return True
        except Http404:
            return False

    def registro(self, nombre, cuentaAdmin, contrasena):
        adminEafit = Usuario(nombre=nombre, cuentaAdmin=cuentaAdmin, contraseña=contrasena)
        adminEafit.save()
        return adminEafit


class AdminPARKIFY(models.Model):
    idAdminPARKIFY = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cuentaAdmin = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)

    def login(self, correo, contrasena):
        try:
            usuario = get_object_or_404(AdminPARKIFY, correo=correo, contrasena=contrasena)
            return True
        except Http404:
            return False

    def registro(self, nombre, cuentaAdmin, contrasena):
        adminParkify = Usuario(nombre=nombre, cuentaAdmin=cuentaAdmin, contraseña=contrasena)
        adminParkify.save()
        return adminParkify

    def testFuncionamiento(self, mecanismo):
        try:
            resultado = mecanismo.prueba()
            return resultado
        except Exception as e:
            # Aquí se podrían agregar acciones para manejar el error,
            # como enviar un correo al equipo de desarrollo o guardar un registro
            # de la falla en una base de datos
            print(f"Error al probar el mecanismo: {e}")
            return False


class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    organizador = models.CharField(max_length=100)

    def informaEvento(self):
        # Función para informar sobre un evento
        pass
