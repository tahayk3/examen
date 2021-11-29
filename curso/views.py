from django.shortcuts import render
from django.contrib import messages
from .forms import MateriaForm
from curso.models import Alumno, Cursa, Materia

def curso_nueva(request):
    if request.method == "POST":
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            materia = Materia.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for alumno_id in request.POST.getlist('actores'):
                actuacion = Cursa(alumno_id=alumno_id, Materia_id = materia.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Curso Guardada Exitosamente')
    else:
        formulario = MateriaForm()
    return render(request, 'materia/materia_editar.html', {'formulario': formulario})