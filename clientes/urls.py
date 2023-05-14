from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [   
    path('clientes/', views.gestionClientes, name='gestionClientes'),
    path('clientes', views.agregarClientes, name='agregarClientes'),
    path('CLIENTES/<int:ID_CLIENTES>/', views.editarCliente, name='editarCliente'),

]