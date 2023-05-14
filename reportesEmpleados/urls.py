from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [   
    path('reportesEmpleado', views.reportesEmpleado, name='reportesEmpleado'),
    path('reportesEmpleados', views.reportesEmpleados, name='reportesEmpleados'),   
    path('reportespormesE', views.reportespormesE, name='reportespormesE'),
    path('dasboardEmpleados', views.dasboardEmpleados, name='dasboardEmpleados'),

]