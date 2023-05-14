from django.db import models

# Create your models here.


class Cliente(models.Model):
    ID_CLIENTES = models.AutoField(verbose_name="ID_CLIENTE", primary_key=True)
    NOMBRE_CLIENTES = models.CharField(
        max_length=150, null=False, verbose_name="NOMBRE_CLIENTE", default="")
    TELEFONO = models.CharField(
        max_length=10, null=False, verbose_name="TELEFONO", default="")
    NIT = models.CharField(max_length=15, null=False,
                           verbose_name="NIT", default="")
    EMAIL_CLIENTE = models.CharField(
        max_length=100, null=True, verbose_name="EMAIL", default="")
    DIRECCION_CLIENTE = models.CharField(
        max_length=200, null=False, verbose_name="DIRECCION", default="")
    ESTATUS = models.CharField(
        max_length=1, null=False, verbose_name="ESTADO", default="A")
    FECHA_ALTA = models.DateTimeField(
        auto_now_add=True, verbose_name="FECHA_ALTA")
    FECHA_ACTUALIZACION = models.DateTimeField(
        auto_now=True, verbose_name="FECHA_ACTUALIZACION")

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.NOMBRE_CLIENTES, self.FECHA_ALTA)

    class Meta:
        db_table = 'CLIENTES'
        # Nombre que tendrá la tabla que se creará en la base de datos
