from django.contrib import admin
from .models import Usuario, Pais, Editorial, Libro, Autor, Prestamo

admin.site.register(Usuario)
admin.site.register(Pais)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Prestamo)
