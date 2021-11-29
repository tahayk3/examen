from django.db import models
from django.contrib import admin

class Alumno(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    actores   = models.ManyToManyField(Alumno, through='Cursa')

    def __str__(self):
        return self.nombre

class Cursa(models.Model):
    actor = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Materia, on_delete=models.CASCADE)

class CursaInLine(admin.TabularInline):
    model = Cursa
    extra = 1


class AlumnoAdmin(admin.ModelAdmin):
    inlines = (CursaInLine,)

class MateriaAdmin (admin.ModelAdmin):
    inlines = (CursaInLine,)