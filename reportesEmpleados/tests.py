from django.test import TestCase

# Create your tests here.
class ReportesEmpleadoTestCase(TestCase):
    def test_reportes_empleado(self):
        # Crea una solicitud HTTP GET para la vista reportesEmpleado
        response = self.client.get(reverse('reportesEmpleado'))

        # Verifica que se haya devuelto una respuesta exitosa
        self.assertEqual(response.status_code, 200)

        # Verifica que se esté utilizando la plantilla correcta
        self.assertTemplateUsed(response, 'REPORTESEMPLEADOS/generareportes.html')

