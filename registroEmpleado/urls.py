from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [   
    path('registroEmpleado/', views.gestionEmpleados, name='gestionEmpleados'),
    path('registroEmpleado', views.registrarEmpleados, name='registrarEmpleados'),
    path('registroEmpleado/<int:ID_EMP>/', views.editarEmpleados, name='editarEmpleados'),
]