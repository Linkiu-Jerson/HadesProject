import datetime
from django.db import models
from .choices import *

class Usuario(models.Model):
    cod_usu = models.AutoField(db_column='Cod_Usu', primary_key=True)
    nom_usu = models.CharField(db_column='Nom_Usu', unique=True, max_length=100, null=False, db_collation='utf8_general_ci', verbose_name='Nombre de Usuario')
    correo = models.CharField(db_column='Correo', unique=True,  max_length=100, null=False, db_collation='utf8_general_ci', verbose_name='Correo Electronico')
    contrasena = models.CharField(db_column='Contrasena', max_length=50, null=False, blank=False, db_collation='utf8_general_ci', verbose_name='Contraseña')
    imagen = models.ImageField(db_column='Imagen', max_length=200, null=True, upload_to='user/%Y/%m', verbose_name='Imagen')

    def __str__(self):
        return self.nom_usu

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
        ordering = ['cod_usu']

class Categoria(models.Model):
    cod_cat = models.AutoField(db_column='Cod_Cat', primary_key=True)
    nom_cat = models.CharField(db_column='Nom_Cat', max_length=50, null=False,  blank=False, verbose_name='Nombre', db_collation='utf8_general_ci')
    imagen = models.ImageField(db_column='Imagen', max_length=200, null=False, upload_to='category/%Y/%m', verbose_name='Imagen')

    def __str__(self):
        return self.nom_cat

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['cod_cat']


class Proveedor(models.Model):
    cod_pro = models.AutoField(db_column='Cod_Pro', primary_key=True)
    cod_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False, db_column='Cod_Usu', verbose_name='Usuario')
    cod_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False, db_column='Cod_Cat', verbose_name='Categoria')
    nom_pro = models.CharField(db_column='Nom_Pro', max_length=100, null=False, db_collation='utf8_general_ci', verbose_name='Proveedor')
    color = models.CharField(db_column='Color', max_length=20, null=False, default='#6F11FF', db_collation='utf8_general_ci', verbose_name='Color')

    def __str__(self):
        return self.nom_pro

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'
        ordering = ['cod_pro']


class Suscripcion(models.Model):
    #Variables globales para la fecha
    fecha_hoy = datetime.date.today()
    fecha_mañana = fecha_hoy + datetime.timedelta(days=1)

    cod_sub = models.AutoField(db_column='Cod_Sub', primary_key=True)
    cod_pro = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='Cod_Pro', null=False, blank=False, verbose_name='Proveedor')
    cod_usu = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='Cod_Usu', null=False, blank=False, verbose_name='Usuario')
    fecha = models.DateField(db_column='Fecha', default=fecha_hoy, null=False, blank=False, verbose_name='Fecha de Suscripcion')
    ciclo = models.CharField(db_column='Ciclo', choices=ciclo_choices, max_length=10, default='monthly', null=False, blank=False, db_collation='utf8_general_ci', verbose_name='Ciclo')
    monto = models.DecimalField(db_column='Monto', default=0.00, max_digits=8, decimal_places=2, null=False, blank=False, verbose_name='Monto a cobrar')
    moneda = models.CharField(db_column='Moneda', default='PEN', max_length=3, null=False, blank=False, db_collation='utf8_general_ci' , verbose_name='Tipo de Moneda')
    recordatorio = models.CharField(db_column='Recordatorio', choices=recordatorio_choices, max_length=20, default='monthly', db_collation='utf8_general_ci', verbose_name='Recordatorio')
    duracion = models.DateField(db_column='Duracion', default=fecha_mañana, null=False, blank=False, verbose_name='Fecha de Termino')
    estado = models.BooleanField(db_column='Estado', default=True, null=False, verbose_name='Estado')

    def __str__(self):
        return '{0} - {1}'.format(str(self.cod_usu), self.fecha)

    class Meta:
        verbose_name = 'Suscripcion'
        verbose_name_plural = 'Suscripciones'
        db_table = 'suscripcion'
        ordering = ['cod_sub']