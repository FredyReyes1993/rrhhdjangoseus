from django.shortcuts import render,get_object_or_404
from .models import Cliente
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def editarCliente(request, ID_CLIENTES):
    cliente = get_object_or_404(Cliente, ID_CLIENTES=ID_CLIENTES)
    
    if request.method == 'POST':
        ncliente = request.POST['txtNombreCliente']
        tcliente = request.POST['txtTelefonoCliente']
        nitcliente = request.POST['txtNitCliente']
        emailcliente = request.POST['txtEmailCliente']
        direcliente = request.POST['txtDireccionCliente']
        estacliente = request.POST['txtestaCliente']

        cliente.NOMBRE_CLIENTES = ncliente
        cliente.TELEFONO = tcliente
        cliente.NIT = nitcliente
        cliente.EMAIL_CLIENTE = emailcliente
        cliente.DIRECCION_CLIENTE = direcliente
        cliente.ESTATUS = estacliente
        cliente.save()

        return HttpResponseRedirect(reverse('gestionClientes'))
    
    return render(request, 'CLIENTES/editarCliente.html', {'cliente': cliente})


def agregarClientes(request):
    if request.method == 'POST':
        ncliente = request.POST['txtNombreCliente']
        tcliente = request.POST['txtTelefonoCliente']
        nitcliente = request.POST['txtNitCliente']
        emailcliente = request.POST['txtEmailCliente']
        direcliente = request.POST['txtDireCliente']

        clienteadd = Cliente.objects.create(
            NOMBRE_CLIENTES=ncliente, TELEFONO=tcliente, NIT=nitcliente, EMAIL_CLIENTE=emailcliente, DIRECCION_CLIENTE=direcliente,ESTATUS='A')

        clienteadd.save()

        return HttpResponseRedirect(reverse('gestionClientes'))

    return render(request, 'CLIENTES/agregarClientes.html')


def gestionClientes(request):
    ListadoClientes = Cliente.objects.all()
    return render(request, 'CLIENTES/gestionClientes.html', {'ListClientes': ListadoClientes})
    # Por medio de ListClientes envio el ListadoClientes a la plantilla HTML





