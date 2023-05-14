from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from datetime import datetime
from reportlab.platypus import  Table, TableStyle
from reportlab.lib import colors
from registroEmpleado.models import Empleado
from django.db.models.functions import Cast
from django.db.models import DateField

def reportesEmpleado(request):
    return render(request, 'REPORTESEMPLEADOS/generareportes.html')

def reportesEmpleados(request):

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'inline; filename="reportes.pdf"'

    p = canvas.Canvas(response, pagesize=landscape(letter))

    p.setTitle("Reportes | Empleados")

    header_img = "imagen/HEAD.png"
    img_width = 800  # Ancho de la imagen
    img_height = 80  # Altura de la imagen
    p.drawImage(header_img, 0, 490, width=img_width,
                height=img_height, preserveAspectRatio=False)

    encabezado = "Reporte Empleados"
    p.setFont("Helvetica", 18)
    p.drawCentredString(400, 480, encabezado)

    now = datetime.now()

    date_string = now.strftime("%d/%m/%Y %H:%M:%S")

    p.setFontSize(10)

    p.drawString(650, 490, date_string)


    empleados = Empleado.objects.all()

    # Agregar una tabla
    data = [['No.', 'Nombre', 'Apellido', 'PLAZA',
             'Teléfono', 'Dirección', 'Estatus'],]

    for empleado in empleados:
        data.append([empleado.ID_EMP, empleado.PNOM, empleado.PAPE,
                     empleado.TCONT, empleado.CELCASA, empleado.DEMP,empleado.ESTATUS])

    table = Table(data)

    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                           ('FONTSIZE', (0, 0), (-1, -1), 10),
                           ('LEADING', (0, 0), (-1, -1), 12),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                           ('BOX', (0, 0), (-1, -1), 0.5, colors.grey),
                           ('WIDTH', (0, 0), (-1, -1), 'AUTO'),
                           ('HEIGHT', (0, 0), (-1, -1), 'AUTO')]))

    # Agregar la tabla al PDF
    table.wrapOn(p, 0, 0)
    table.drawOn(p, 20, 400)

    # Agregar una imagen en el footer con un tamaño mayor

    footer_img = "imagen/Footer.png"
    img_width = 800  # Ancho de página carta
    img_height = 100  # Altura de la imagen
    p.drawImage(footer_img, 0, 0, width=img_width,
                height=img_height, preserveAspectRatio=True)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # Devolver la respuesta HTTP con el contenido del PDF
    return response

 
def reportespormesE(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reportes.pdf"'
    
    p = canvas.Canvas(response, pagesize=landscape(letter))
    p.setTitle("Reportes | Empleados")

    # Agregar una imagen en el encabezado
    header_img = "imagen/HEAD.png"
    img_width = 800  # Ancho de la imagen
    img_height = 80  # Altura de la imagen
    p.drawImage(header_img, 0, 490, width=img_width,
                height=img_height, preserveAspectRatio=False)

    encabezado = "Reporte Empleados"
    p.setFont("Helvetica", 18)
    p.drawCentredString(400, 480, encabezado)

    # Obtener la fecha y hora actual en formato datetime
    now = datetime.now()
    # Formatear la fecha y hora como una cadena
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # Establecer la fuente y el tamaño de fuente para la fecha
    p.setFontSize(10)
    # Agregar la fecha al PDF
    p.drawString(650, 490, date_string)

    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if fecha_inicio and fecha_fin:
        fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
        empleados = Empleado.objects.filter(FALTA__range=(
            f"{fecha_inicio} 00:00:00", f"{fecha_fin} 23:59:59"))
    else:
        empleados = Empleado.objects.all()
 

    # Agregar una tabla
    data = [['No.', 'Nombre', 'Apellido', 'PLAZA',
             'Teléfono', 'Dirección','Fecha Alta', 'Estatus'],]

    for empleado in empleados:
        data.append([empleado.ID_EMP, empleado.PNOM, empleado.PAPE,
                     empleado.TCONT, empleado.CELCASA, empleado.DEMP,empleado.FALTA,empleado.ESTATUS])

    table = Table(data)

    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                           ('FONTSIZE', (0, 0), (-1, -1), 10),
                           ('LEADING', (0, 0), (-1, -1), 12),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                           ('BOX', (0, 0), (-1, -1), 0.5, colors.grey),
                           ('WIDTH', (0, 0), (-1, -1), 'AUTO'),
                           ('HEIGHT', (0, 0), (-1, -1), 'AUTO')]))

    # Agregar la tabla al PDF
    table.wrapOn(p, 0, 0)
    table.drawOn(p, 20, 400)

    # Agregar una imagen en el footer con un tamaño mayor

    footer_img = "imagen/Footer.png"
    img_width = 800  # Ancho de página carta
    img_height = 100  # Altura de la imagen
    p.drawImage(footer_img, 0, 0, width=img_width,
                height=img_height, preserveAspectRatio=True)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # Devolver la respuesta HTTP con el contenido del PDF
    return response



def  dasboardEmpleados(request):
    # Obtenemos los clientes por mes utilizando annotate

    formato_fecha = '%Y-%m-%d' # Asumiendo que el formato de la fecha en la cadena es 'YYYY-MM-DD'

    empleados_por_mes = Empleado.objects.annotate(month=TruncMonth(Cast('FALTA', DateField(formato_fecha)))).values('month').annotate(total=Count('ID_EMP'))
    # Creamos una lista con las etiquetas para el eje x del gráfico
    etiquetas = [datetime.strftime(c['month'], '%B') for c in empleados_por_mes]
    # Creamos una lista con los datos para el eje y del gráfico
    datos = [c['total'] for c in empleados_por_mes]
    # Pasamos los datos a la plantilla

    return render(request, 'REPORTESEMPLEADOS/dasboardEmpleados.html', {'etiquetas': etiquetas, 'datos': datos})