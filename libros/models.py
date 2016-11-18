from django.db import models
from django.contrib import admin

class Usuario(models.Model):
    dpi = models.CharField(max_length=13)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombreP = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreP

class Editorial(models.Model):
    nombreE = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreE

class Autor(models.Model):
    nombreA = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreA

class Libro(models.Model):
    isbn = models.CharField(max_length=13)
    titulo = models.CharField(max_length=200)
    #portada = models.ImageField() se usar el campo de tipo imagen
    autor = models.ForeignKey(Autor, null=True, blank=True)
    editorial = models.ForeignKey(Editorial, null=True, blank=True)
    pais = models.ForeignKey(Pais, null=True, blank=True)
    anio = models.CharField(max_length=5)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    idprestamo = models.CharField(max_length=200)
    usuariop = models.ForeignKey(Usuario, null=True, blank=True)
    fechaI = models.DateTimeField(blank=True, null=True)
    fechaF = models.DateTimeField(blank=True, null=True)
    librop   = models.ManyToManyField(Libro, through='Detalle')

    def __str__(self):
        return self.idprestamo

class Detalle(models.Model):
    prestamop = models.ForeignKey(Prestamo, null=True, blank=True)
    librop = models.ForeignKey(Libro, null=True, blank=True)

class DetalleInLine(admin.TabularInline):
    model = Detalle
    extra = 1


class LibroAdmin(admin.ModelAdmin):
    inlines = (DetalleInLine,)


class PrestamoAdmin (admin.ModelAdmin):
    inlines = (DetalleInLine,)
