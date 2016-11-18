from django import forms
from .models import Libro, Prestamo

class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = ('usuariop', 'fechaI', 'librop',)

    def __init__ (self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)
        self.fields["librop"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["librop"].help_text = "Ingrese los Libros a prestar"
        self.fields["librop"].queryset = Libro.objects.all()
