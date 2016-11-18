from django.db import models

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
    estado = models.CharField(max_length=200)
    prestamista = models.ForeignKey(Usuario, null=True, blank=True)

    def __str__(self):
        return self.isbn
