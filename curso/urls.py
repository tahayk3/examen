from django.conf.urls import url
from . import views

urlpatterns = [
    url('curso_lista/lista', views.Curso, name ='curso_lista'),
    url('', views.curso_nueva, name='curso_nueva'),
    ]

    