from django.shortcuts import render
from django.contrib import messages
from .forms import MateriaForm
from curso.models import Cursa, Materia

def curso_nueva(request):
    if request.method == "POST":
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            pelicula = Materia.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for actor_id in request.POST.getlist('actores'):
                actuacion = Cursa(actor_id=actor_id, pelicula_id = pelicula.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = MateriaForm()
    return render(request, 'curso/curso_nueva.html', {'formulario': formulario})