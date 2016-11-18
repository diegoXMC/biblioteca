from django.contrib import messages, admin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Libro, Usuario, Pais, Editorial, Autor
from .forms import Prestamo
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect

def agregar(request, pkl):
    qlibro = Libro.objects.filter(pk=pkl)
    return render(request, 'prestamo.html', {'formulario': formulario, 'qlibro':qlibro})


def prestamo(request):
    if request.method == "POST":
        formulario = Prstamo(request.POST)
        if formulario.is_valid():
            libro = Libros.objects.create(creador=cre, Titulo=formulario.cleaned_data['Titulo'], Genero=formulario.cleaned_data['Genero'], Resena=formulario.cleaned_data['Resena'])
            for autor_id in request.POST.getlist('Autor'):
                actuacion = Asignacion(Libro=libro.Titulo, Autor=autor_id)
                actuacion.save()
            return redirect('libros.views.agregar')
    else:
        formulario = Prestamo()
    return render(request, 'prestamo.html', {'formulario': formulario})
