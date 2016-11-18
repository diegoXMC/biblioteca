from django.contrib import messages, admin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Libro, Usuario, Pais, Editorial, Autor, Prestamo, Detalle
from .forms import PrestamoForm
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect

def prestamo(request):
    if request.method == "POST":
        formulario = PrestamoForm(request.POST)
        if formulario.is_valid():
            cp=Prestamo.objects.count()
            pres = Prestamo.objects.create(idprestamo=cp,usuariop=formulario.cleaned_data['usuariop'], fechaI = formulario.cleaned_data['fechaI'])
            pres.save()
            for libro_id in request.POST.getlist('librop'):
                detalle = Detalle(prestamop=pres.id, librop=libro_id)
                detalle.save()
            messages.add_message(request, messages.SUCCESS, 'Prestamo Realizado Exitosamente')
    else:
        formulario = PrestamoForm()
    return render(request, 'prestamo.html', {'formulario': formulario})
