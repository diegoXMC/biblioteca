from django.contrib import admin
from .models import Usuario, Pais, Editorial, Libro, Autor

admin.site.register(Usuario)
admin.site.register(Pais)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Libro)
