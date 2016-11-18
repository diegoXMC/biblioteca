from django import forms

from .models import Libro

class Prestamo(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ('isbn', 'titulo', 'autor', 'editorial', 'pais', 'anio', 'prestamista',)
