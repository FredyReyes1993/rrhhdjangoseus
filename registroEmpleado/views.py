from django.shortcuts import render, get_object_or_404
from .models import Empleado
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage()

# Create your views here.


def editarEmpleados(request, ID_EMP):
    empleado = get_object_or_404(Empleado, ID_EMP=ID_EMP)

    if request.method == 'POST':
        ftipodoc = request.POST['id_tipo_documento']
        fdocIden = request.POST['txtdocIde']
        fdepDPI = request.POST['id_departamento_dpi']
        fmunDPI = request.POST['id_municipio_dpi']
        fnombre = request.POST['txtpnombre']
        fsnombre = request.POST['txtsenombre']
        fpapellido = request.POST['txtpape']
        fsapellido = request.POST['txtsape']
        fApecasada = request.POST['txtAcasa']
        fgenero = request.POST['id_genero']
        ffecnac = request.POST['txtfenac']
        festcivil = request.POST['id_civil']
        fnacionalidad = request.POST['id_nacionalidad']
        fdeptonac = request.POST['id_depto_nac']
        fmunac = request.POST['id_muni_nac']
        ffechaalta = request.POST['txtfechalta']
        ftcont = request.POST['txttcont']
        ffinal = request.POST['txtffinal']
        fdirec = request.POST['txtdirec']
        fzona = request.POST['txtzona']
        fdeptodom = request.POST['id_depto_dom']
        fmunidom = request.POST['id_muni_dom']
        ftelcasa = request.POST['txttelcasa']
        fcel = request.POST['txtcel']
        fcorreo = request.POST['txtcorreo']
        fniedu = request.POST['id_niveleducativo']
        fgradaca = request.POST['id_gradoacademico']
        fcenedu = request.POST['txtcenedu']
        fobser1 = request.POST['txtobser']
        flista1 = request.POST['id_Lista1']
        fnompar = request.POST['txtnompar']
        fapepar = request.POST['txtapepar']
        fdirepar = request.POST['txtdirepar']
        ftelpar = request.POST['txttelpar']
        flista2 = request.POST['id_Lista2']
        fnompar1 = request.POST['txtnompar1']
        fapepar1 = request.POST['txtapepar1']
        fdirepar1 = request.POST['txtdirepar1']
        ftelpar1 = request.POST['txttelpar1']
        flista3 = request.POST['id_Lista3']
        fnompar2 = request.POST['txtnompar2']
        fapepar2 = request.POST['txtapepar2']
        fdirepar2 = request.POST['txtdirepar2']
        ftelpar2 = request.POST['txttelpar2']
        fnpenal = request.POST['txtnnpenal']
        ffechapenal = request.POST['fechapenales']
        ffechavenpenal = request.POST['fechavenpenal']
        fnpolicial = request.POST['txtnnpolicial']
        ffechapolicial = request.POST['fechapoliciales']
        ffechavenpolicial = request.POST['fechavenpoli']
        fgrupobla = request.POST['id_Gpobla']
        fcomLin = request.POST['id_comLin']
        fAigss = request.POST['txtAigss']
        fnit = request.POST['txtNIT']
        fAirtra = request.POST['txtAirta']
        foficio = request.POST['txtoficio']
        ftipoexp = request.POST['id_tipo_exp']
        fpuesexp = request.POST['id_puesto_exp']
        ftipoLic = request.POST['id_tipoLic']
        fnLic = request.POST['txtNLic']
        ffechavenlic = request.POST['fechavenlic']
        fsalmen = request.POST['txtSalbm']
        fbonoinc = request.POST['txtboninc']
        fjornlab = request.POST['id_jorlab']
        ftipopago = request.POST['id_tipopag']

        empleado.TDOC = ftipodoc
        empleado.NDOC = fdocIden
        empleado.DDOC = fdepDPI
        empleado.MDOC = fmunDPI
        empleado.PNOM = fnombre
        empleado.SNOM = fsnombre
        empleado.PAPE = fpapellido
        empleado.SAPE = fsapellido
        empleado.ACAS = fApecasada
        empleado.GEN = fgenero
        empleado.FNAC = ffecnac
        empleado.ECIVIL = festcivil
        empleado.NNAC = fnacionalidad
        empleado.DNAC = fdeptonac
        empleado.MNAC = fmunac
        empleado.FALTA = ffechaalta
        empleado.TCONT = ftcont
        empleado.FFINAL = ffinal
        empleado.DEMP = fdirec
        empleado.ZONA = fzona
        empleado.DDOM = fdeptodom
        empleado.MDOM = fmunidom
        empleado.TELCASA = ftelcasa
        empleado.CELCASA = fcel
        empleado.EMAIL = fcorreo
        empleado.NEDUC = fniedu
        empleado.GRAC = fgradaca
        empleado.NOMCENTRO = fcenedu
        empleado.OBSER = fobser1
        empleado.PAR_1 = flista1
        empleado.PNOM1 = fnompar
        empleado.PAPE1 = fapepar
        empleado.PDIRE1 = fdirepar
        empleado.PTEL1 = ftelpar
        empleado.PAR_2 = flista2
        empleado.PNOM2 = fnompar1
        empleado.PAPE2 = fapepar1
        empleado.PDIRE2 = fdirepar1
        empleado.PTEL2 = ftelpar1
        empleado.PAR_3 = flista3
        empleado.PNOM3 = fnompar2
        empleado.PAPE3 = fapepar2
        empleado.PDIRE3 = fdirepar2
        empleado.PTEL3 = ftelpar2
        empleado.NOSERPEN = fnpenal
        empleado.FEMPEN = ffechapenal
        empleado.FVEPEN = ffechavenpenal
        empleado.NOSERPOL = fnpolicial
        empleado.FEMPOL = ffechapolicial
        empleado.FVEPOL = ffechavenpolicial
        empleado.GRUPO = fgrupobla
        empleado.COMLIN = fcomLin
        empleado.AIGSS = fAigss
        empleado.ANIT = fnit
        empleado.AIRTRA = fAirtra
        empleado.POFICIO = foficio
        empleado.TEXPE = ftipoexp
        empleado.PEMPLE = fpuesexp
        empleado.TLIC = ftipoLic
        empleado.NOLIC = fnLic
        empleado.FVLIC = ffechavenlic
        empleado.SBM = fsalmen
        empleado.BINC = fbonoinc
        empleado.JORLAB = fjornlab
        empleado.TIPAGO = ftipopago
        #empleado.ESTATUS =
        #empleado.MBAJA =
        empleado.save()

        return HttpResponseRedirect(reverse(gestionEmpleados))
    
    return render(request, 'EMPLEADOS/editarEmpleados.html',{'empleado':empleado})



def registrarEmpleados(request):
    if request.method == 'POST':
        fimagen = request.FILES['txtimgInp']
        fotofile = fs.save(fimagen.name, fimagen)
        ftipodoc = request.POST['id_tipo_documento']
        fdocIden = request.POST['txtdocIde']
        fdepDPI = request.POST['id_departamento_dpi']
        fmunDPI = request.POST['id_municipio_dpi']
        fnombre = request.POST['txtpnombre']
        fsnombre = request.POST['txtsenombre']
        fpapellido = request.POST['txtpape']
        fsapellido = request.POST['txtsape']
        fApecasada = request.POST['txtAcasa']
        fgenero = request.POST['id_genero']
        ffecnac = request.POST['txtfenac']
        festcivil = request.POST['id_civil']
        fnacionalidad = request.POST['id_nacionalidad']
        fdeptonac = request.POST['id_depto_nac']
        fmunac = request.POST['id_muni_nac']
        ffechaalta = request.POST['txtfechalta']
        ftcont = request.POST['txttcont']
        ffinal = request.POST['txtffinal']
        fdirec = request.POST['txtdirec']
        fzona = request.POST['txtzona']
        fdeptodom = request.POST['id_depto_dom']
        fmunidom = request.POST['id_muni_dom']
        ftelcasa = request.POST['txttelcasa']
        fcel = request.POST['txtcel']
        fcorreo = request.POST['txtcorreo']
        fniedu = request.POST['id_niveleducativo']
        fgradaca = request.POST['id_gradoacademico']
        fcenedu = request.POST['txtcenedu']
        fobser1 = request.POST['txtobser']
        flista1 = request.POST['id_Lista1']
        fnompar = request.POST['txtnompar']
        fapepar = request.POST['txtapepar']
        fdirepar = request.POST['txtdirepar']
        ftelpar = request.POST['txttelpar']
        flista2 = request.POST['id_Lista2']
        fnompar1 = request.POST['txtnompar1']
        fapepar1 = request.POST['txtapepar1']
        fdirepar1 = request.POST['txtdirepar1']
        ftelpar1 = request.POST['txttelpar1']
        flista3 = request.POST['id_Lista3']
        fnompar2 = request.POST['txtnompar2']
        fapepar2 = request.POST['txtapepar2']
        fdirepar2 = request.POST['txtdirepar2']
        ftelpar2 = request.POST['txttelpar2']
        fnpenal = request.POST['txtnnpenal']
        ffechapenal = request.POST['fechapenales']
        ffechavenpenal = request.POST['fechavenpenal']
        fnpolicial = request.POST['txtnnpolicial']
        ffechapolicial = request.POST['fechapoliciales']
        ffechavenpolicial = request.POST['fechavenpoli']
        fgrupobla = request.POST['id_Gpobla']
        fcomLin = request.POST['id_comLin']
        fAigss = request.POST['txtAigss']
        fnit = request.POST['txtNIT']
        fAirtra = request.POST['txtAirta']
        foficio = request.POST['txtoficio']
        ftipoexp = request.POST['id_tipo_exp']
        fpuesexp = request.POST['id_puesto_exp']
        ftipoLic = request.POST['id_tipoLic']
        fnLic = request.POST['txtNLic']
        ffechavenlic = request.POST['fechavenlic']
        fsalmen = request.POST['txtSalbm']
        fbonoinc = request.POST['txtboninc']
        fjornlab = request.POST['id_jorlab']
        ftipopago = request.POST['id_tipopag']

        empleadoadd = Empleado.objects.create(FOTO=fotofile, TDOC=ftipodoc, NDOC=fdocIden, DDOC=fdepDPI, MDOC=fmunDPI, PNOM=fnombre, SNOM=fsnombre,
                                              PAPE=fpapellido, SAPE=fsapellido, ACAS=fApecasada, GEN=fgenero, FNAC=ffecnac, ECIVIL=festcivil,
                                              NNAC=fnacionalidad, DNAC=fdeptonac, MNAC=fmunac, FALTA=ffechaalta, TCONT=ftcont, FFINAL=ffinal, DEMP=fdirec,
                                              ZONA=fzona, DDOM=fdeptodom, MDOM=fmunidom, TELCASA=ftelcasa, CELCASA=fcel, EMAIL=fcorreo, NEDUC=fniedu,
                                              GRAC=fgradaca, NOMCENTRO=fcenedu, OBSER=fobser1, PAR_1=flista1, PNOM1=fnompar, PAPE1=fapepar,
                                              PDIRE1=fdirepar, PTEL1=ftelpar1, PAR_2=flista2, PNOM2=fnompar1, PAPE2=fapepar1,
                                              PDIRE2=fdirepar1, PTEL2=ftelpar, PAR_3=flista3, PNOM3=fnompar2, PAPE3=fapepar2,
                                              PDIRE3=fdirepar2, PTEL3=ftelpar2, NOSERPEN=fnpenal, FEMPEN=ffechapenal, FVEPEN=ffechavenpenal,
                                              NOSERPOL=fnpolicial, FEMPOL=ffechapolicial, FVEPOL=ffechavenpolicial, GRUPO=fgrupobla,
                                              COMLIN=fcomLin, AIGSS=fAigss, ANIT=fnit, AIRTRA=fAirtra, POFICIO=foficio, TEXPE=ftipoexp,
                                              PEMPLE=fpuesexp, TLIC=ftipoLic, NOLIC=fnLic, FVLIC=ffechavenlic, SBM=fsalmen,
                                              BINC=fbonoinc, JORLAB=fjornlab, TIPAGO=ftipopago)

        empleadoadd.save()

        return HttpResponseRedirect(reverse('gestionEmpleados'))

    return render(request, 'EMPLEADOS/registrarEmpleados.html')


def gestionEmpleados(request):
    ListadoEmpleados = Empleado.objects.all()

    return render(request, 'EMPLEADOS/gestionEmpleados.html', {'ListEmpleados': ListadoEmpleados})
    # Por medio de ListEmpleados envio el ListadoEmpleados a la plantilla HTML
