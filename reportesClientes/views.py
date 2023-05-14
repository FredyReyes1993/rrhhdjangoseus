
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from datetime import datetime
from reportlab.platypus import  Table, TableStyle
from reportlab.lib import colors
from clientes.models import Cliente



# Create your views here.
def reportesCliente(request):
    return render(request, 'REPORTESCLIENTES/generareportes.html')


def reportesClientes(request):
    # Crear una respuesta HTTP con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    # para descargar todo
    # response['Content-Disposition'] = 'attachment; filename="hello_world.pdf"'
    # Sirve para visualizar el pdf creado
    response['Content-Disposition'] = 'inline; filename="reportes.pdf"'

    # Crear el objeto Canvas con el tamaño de página carta
    #p = canvas.Canvas(response, pagesize=letter)
    p = canvas.Canvas(response, pagesize=landscape(letter))

    # Establecer el título del PDF
    p.setTitle("Reportes | Clientes")
    # Agregar encabezado centrado en cada página

    # Agregar una imagen en el encabezado
    header_img = "imagen/HEAD.png"
    img_width = 800  # Ancho de la imagen
    img_height = 80  # Altura de la imagen
    p.drawImage(header_img, 0, 490, width=img_width,
                height=img_height, preserveAspectRatio=False)

    encabezado = "Reporte Clientes"
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

    # Query the clients from your database
    clientes = Cliente.objects.all()

    # Agregar una tabla
    data = [['No.', 'Nombre', 'Teléfono', 'Nit',
             'Email', 'Dirección', 'Estatus'],]

    for cliente in clientes:
        data.append([cliente.ID_CLIENTES, cliente.NOMBRE_CLIENTES, cliente.TELEFONO,
                     cliente.NIT, cliente.EMAIL_CLIENTE, cliente.DIRECCION_CLIENTE, cliente.ESTATUS])

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

    # return render (request,'REPORTESCLIENTES/reportesClientes.html')


def reportespormes(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reportes.pdf"'
    
    p = canvas.Canvas(response, pagesize=landscape(letter))
    p.setTitle("Reportes | Clientes")

    # Agregar una imagen en el encabezado
    header_img = "imagen/HEAD.png"
    img_width = 800  # Ancho de la imagen
    img_height = 80  # Altura de la imagen
    p.drawImage(header_img, 0, 490, width=img_width,
                height=img_height, preserveAspectRatio=False)

    encabezado = "Reporte Clientes"
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
        clientes = Cliente.objects.filter(FECHA_ALTA__range=(
            f"{fecha_inicio} 00:00:00", f"{fecha_fin} 23:59:59"))
    else:
        clientes = Cliente.objects.all()
        print(clientes.query)  # imprime la consulta SQL generada por Django
        print(clientes)
        print(fecha_inicio)
        print(fecha_fin)

    # Agregar una tabla
    data = [['No.', 'Nombre', 'Teléfono', 'Nit',
             'Email', 'Dirección', 'Estatus', 'Fecha'],]

    for cliente in clientes:
        fecha_alta = cliente.FECHA_ALTA.strftime('%d/%m/%Y')
        data.append([cliente.ID_CLIENTES, cliente.NOMBRE_CLIENTES, cliente.TELEFONO,
                     cliente.NIT, cliente.EMAIL_CLIENTE, cliente.DIRECCION_CLIENTE, cliente.ESTATUS, fecha_alta])

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

    # return render (request,'REPORTESCLIENTES/reportesClientes.html')



def  dasboardClientes(request):
    # Obtenemos los clientes por mes utilizando annotate
    clientes_por_mes = Cliente.objects.annotate(month=TruncMonth('FECHA_ALTA')).values('month').annotate(total=Count('ID_CLIENTES'))
    # Creamos una lista con las etiquetas para el eje x del gráfico
    etiquetas = [datetime.strftime(c['month'], '%B') for c in clientes_por_mes]
    # Creamos una lista con los datos para el eje y del gráfico
    datos = [c['total'] for c in clientes_por_mes]
    # Pasamos los datos a la plantilla

    return render(request, 'REPORTESCLIENTES/dasboardClientes.html', {'etiquetas': etiquetas, 'datos': datos})