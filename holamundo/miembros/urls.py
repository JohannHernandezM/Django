from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='newMember'),
    path('read', views.read, name='getMembers')
       
    #path('ruta1', views.ruta1, name='ruta1'),
    #path('ruta2', views.ruta2, name='ruta2'),
    #path('pacientes', views.datosPacientes, name='datosPacientes')

]
