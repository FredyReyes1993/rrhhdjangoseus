from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [   
    path('reportesCliente', views.reportesCliente, name='reportesCliente'),
    path('reportesClientes', views.reportesClientes, name='reportesClientes'),
    path('reportespormes', views.reportespormes, name='reportespormes'),
    path('dasboardClientes', views.dasboardClientes, name='dasboardClientes'),

]