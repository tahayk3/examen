from django import forms
from .models import Materia,Alumno


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('nombre', 'anio', 'actores')

    def __init__ (self, *args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields["actores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["actores"].help_text = "Ingrese los alumnos del curso"
        self.fields["actores"].queryset = Alumno.objects.all()