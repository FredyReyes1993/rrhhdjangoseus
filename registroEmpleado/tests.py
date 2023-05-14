from django.test import TestCase, Client,RequestFactory
from django.urls import reverse
from .models import Empleado
from .views import gestionEmpleados
from .views import editarEmpleados, registrarEmpleados

# Create your tests here.
