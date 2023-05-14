from django.db import models

# Create your models here.


class Empleado(models.Model):

	ID_EMP = models.AutoField(verbose_name="ID_EMPLEADO", primary_key=True)
    
	FOTO = models.ImageField(upload_to= 'photos/empleados', blank= True)

	TDOC = models.CharField(max_length=15, null=True,
	                        verbose_name="TIPO_DOCUMENTO", default="")
	NDOC = models.CharField(max_length=13, null=True,
	                        verbose_name="DPI", default="", unique=True)
	DDOC = models.CharField(max_length=50, null=True,
	                        verbose_name="DEPTO_DPI", default="")
	MDOC = models.CharField(max_length=50, null=True,
	                        verbose_name="MUN_DPI", default="")
	PNOM = models.CharField(max_length=50, null=True,
	                        verbose_name="PRIMER_NOMBRE", default="")
	SNOM = models.CharField(max_length=50, null=True,
	                        verbose_name="SEGUNDO_NOMBRE", default="")
	PAPE = models.CharField(max_length=50, null=True,
	                        verbose_name="PRIMER_APELLIDO", default="")
	SAPE = models.CharField(max_length=50, null=True,
	                        verbose_name="SEGUNDO_APELLIDO", default="")
	ACAS = models.CharField(max_length=50, null=True,
	                        verbose_name="APELLIDO_CASADA", default="")
	GEN = models.CharField(max_length=20, null=True,
	                       verbose_name="GENERO", default="")
	FNAC = models.CharField(max_length=10, null=True,
	                        verbose_name="FECHA_NAC", default="")
	ECIVIL = models.CharField(max_length=25, null=True,
	                          verbose_name="ESTADO_CIVIL", default="")
	NNAC = models.CharField(max_length=50, null=True,
	                        verbose_name="NAC_NACIMIENTO", default="")
	DNAC = models.CharField(max_length=50, null=True,
	                        verbose_name="DEPTO_NACIMIENTO", default="")
	MNAC = models.CharField(max_length=50, null=True,
	                        verbose_name="MUN_NACIMIENTO", default="")
	FALTA = models.CharField(max_length=10, null=True,
	                         verbose_name="FECHA_ALTA", default="")
	TCONT = models.CharField(max_length=25, null=True,
	                         verbose_name="TIPO_CONTRATO", default="")
	FFINAL = models.CharField(max_length=10, null=True,
	                          verbose_name="FECHA_FINAL", default="")
	DEMP = models.CharField(max_length=250, null=True,
	                        verbose_name="DIRECCION", default="")
	ZONA = models.CharField(max_length=10, null=True,
	                        verbose_name="ZONA", default="")
	DDOM = models.CharField(max_length=50, null=True,
	                        verbose_name="DEPTO_DOM", default="")
	MDOM = models.CharField(max_length=50, null=True,
	                        verbose_name="MUN_DOM", default="")
	TELCASA = models.CharField(max_length=10, null=True,
	                           verbose_name="TEL_CASA", default="")
	CELCASA = models.CharField(max_length=10, null=True,
	                           verbose_name="CEL_CASA", default="")
	EMAIL = models.CharField(max_length=100, null=True,
	                         verbose_name="EMAIL", default="")
	NEDUC = models.CharField(max_length=25, null=True,
	                         verbose_name="N_EDUC", default="")
	GRAC = models.CharField(max_length=25, null=True,
	                        verbose_name="GRADO", default="")
	NOMCENTRO = models.CharField(
	    max_length=100, null=True, verbose_name="CENTRO", default="")
	OBSER = models.CharField(max_length=250, null=True,
	                         verbose_name="OBSERVACIONES", default="")
	PAR_1 = models.CharField(max_length=10, null=True,
	                         verbose_name="PARENTESCO", default="")
	PNOM1 = models.CharField(max_length=50, null=True,
	                         verbose_name="P_NOMBRE", default="")
	PAPE1 = models.CharField(max_length=50, null=True,
	                         verbose_name="P_APELLIDO", default="")
	PDIRE1 = models.CharField(max_length=100, null=True,
	                          verbose_name="DIRECCION", default="")
	PTEL1 = models.CharField(max_length=10, null=True,
	                         verbose_name="TELEFONO", default="")
	PAR_2 = models.CharField(max_length=10, null=True,
	                         verbose_name="PARENTESCO", default="")
	PNOM2 = models.CharField(max_length=50, null=True,
	                         verbose_name="P_NOMBRE", default="")
	PAPE2 = models.CharField(max_length=50, null=True,
	                         verbose_name="P_APELLIDO", default="")
	PDIRE2 = models.CharField(max_length=100, null=True,
	                          verbose_name="DIRECCION", default="")
	PTEL2 = models.CharField(max_length=10, null=True,
	                         verbose_name="TELEFONO", default="")
	PAR_3 = models.CharField(max_length=10, null=True,
	                         verbose_name="PARENTESCO", default="")
	PNOM3 = models.CharField(max_length=50, null=True,
	                         verbose_name="P_NOMBRE", default="")
	PAPE3 = models.CharField(max_length=50, null=True,
	                         verbose_name="P_APELLIDO", default="")
	PDIRE3 = models.CharField(max_length=100, null=True,
	                          verbose_name="DIRECCION", default="")
	PTEL3 = models.CharField(max_length=10, null=True,
	                         verbose_name="TELEFONO", default="")
	NOSERPEN = models.CharField(
	    max_length=25, null=True, verbose_name="NO_SERIE_PENAL", default="")
	FEMPEN = models.CharField(max_length=25, null=True,
	                          verbose_name="FECHA_EM_PENAL", default="")
	FVEPEN = models.CharField(max_length=25, null=True,
	                          verbose_name="FECHA_VEN_PENAL", default="")
	NOSERPOL = models.CharField(
	    max_length=25, null=True, verbose_name="NO_SERIE", default="")
	FEMPOL = models.CharField(max_length=25, null=True,
	                          verbose_name="FECHA_EM_POLICIAL", default="")
	FVEPOL = models.CharField(max_length=25, null=True,
	                          verbose_name="FECHA_VEN_POLICIAL", default="")
	GRUPO = models.CharField(max_length=25, null=True,
	                         verbose_name="GRUPO_POBLACIONAL", default="")
	COMLIN = models.CharField(max_length=100, null=True,
	                          verbose_name="COM_LIN", default="")
	AIGSS = models.CharField(max_length=15, null=True,
	                         verbose_name="A_IGSS", default="")
	ANIT = models.CharField(max_length=15, null=True,
	                        verbose_name="A_NIT", default="")
	AIRTRA = models.CharField(max_length=15, null=True,
	                          verbose_name="A_IRTA", default="")
	POFICIO = models.CharField(max_length=50, null=True,
	                           verbose_name="P_OFICIO", default="")
	TEXPE = models.CharField(max_length=50, null=True,
	                         verbose_name="T_EXPEDIENTE", default="")
	PEMPLE = models.CharField(max_length=50, null=True,
	                          verbose_name="PUESTO", default="")
	TLIC = models.CharField(max_length=2, null=True,
	                        verbose_name="TIPO_LICENCIA", default="")
	NOLIC = models.CharField(max_length=15, null=True,
	                         verbose_name="NO_LIC", default="")
	FVLIC = models.CharField(max_length=10, null=True,
	                         verbose_name="VENC_LICENCIA", default="")
	SBM = models.CharField(max_length=15, null=True,
	                       verbose_name="BASE_MENSUAL", default="")
	BINC = models.CharField(max_length=15, null=True,
	                        verbose_name="BONO_INC", default="")
	JORLAB = models.CharField(max_length=50, null=True,
	                          verbose_name="JOR_LABORAL", default="")
	TIPAGO = models.CharField(max_length=25, null=True,
	                          verbose_name="TIPO_PAGO", default="")
	ESTATUS = models.CharField(max_length=1, null=True,
	                           verbose_name="ESTADO", default="A")
	MBAJA = models.CharField(max_length=500, null=True,
	                         verbose_name="MOTIVO_DESPIDO", default="")
	FACTUAL = models.DateTimeField(auto_now=True, verbose_name="FECHA_ACTUAL")

def __str__(self):
      return self.PNOM

class Meta:
    db_table = 'EMPLEADOS'
    # Nombre que tendrá la tabla que se creará en la base de datos