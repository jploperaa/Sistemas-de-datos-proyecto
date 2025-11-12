# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Catalogo(models.Model):
    id_catalogo = models.AutoField(db_column='ID_catalogo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'Catalogo'


class ClubLectura(models.Model):
    id_club = models.AutoField(db_column='ID_club', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    fecha_creacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'Club_lectura'


class Intercambio(models.Model):
    id_intercambio = models.AutoField(db_column='ID_intercambio', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_usuario')  # Field name made lowercase.
    id_libro = models.ForeignKey('Libro', models.DO_NOTHING, db_column='ID_libro')  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=20)
    class Meta:
        managed = False
        db_table = 'Intercambio'
        unique_together = (('id_libro', 'isbn'),)


class Libro(models.Model):
    id_libro = models.IntegerField(primary_key=True, db_column='ID_libro')
    isbn = models.CharField(db_column='ISBN', max_length=20)
    titulo = models.CharField(db_column='titulo', max_length=200)
    autor = models.CharField(db_column='autor', max_length=150)
    anio_publicacion = models.IntegerField(db_column='año_publicacion', blank=True, null=True)
    genero = models.CharField(db_column='genero', max_length=80, blank=True, null=True)
    modalidad = models.CharField(db_column='modalidad', max_length=40, blank=True, null=True)
    resumen = models.TextField(db_column='resumen', blank=True, null=True)
    propietario = models.CharField(db_column='propietario', max_length=120, blank=True, null=True)
    id_usuario_recibe = models.IntegerField(db_column='ID_usuario_recibe', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'Libro'
        unique_together = (('id_libro', 'isbn'),)


class Publicacion(models.Model):
    id_publicacion = models.AutoField(db_column='ID_publicacion', primary_key=True)  # Field name made lowercase.
    modalidad = models.CharField(max_length=40, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_usuario')  # Field name made lowercase.
    id_catalogo = models.ForeignKey(Catalogo, models.DO_NOTHING, db_column='ID_catalogo')  # Field name made lowercase.
    id_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='ID_libro')  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=20)

    class Meta:
        managed = False
        db_table = 'Publicacion'


class Resea(models.Model):
    id_reseña = models.AutoField(db_column='ID_reseña', primary_key=True)  # Field name made lowercase.
    calificacion = models.IntegerField(blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    fecha_reseña = models.DateField(blank=True, null=True)
    id_usuario_autor = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_usuario_autor')  # Field name made lowercase.
    id_usuario_comenta = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_usuario_comenta', related_name='resea_id_usuario_comenta_set', blank=True, null=True)  # Field name made lowercase.
    id_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='ID_libro')  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=20)

    class Meta:
        managed = False
        db_table = 'Reseña'


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='ID_usuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    correo = models.CharField(unique=True, max_length=120, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuario'


class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True, db_column='ID_venta')
    fecha_venta = models.DateField(db_column='fecha_venta', blank=True, null=True)
    estado = models.CharField(db_column='estado', max_length=30)
    precio = models.DecimalField(db_column='precio', max_digits=10, decimal_places=2)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_usuario')
    id_libro = models.ForeignKey('Libro', models.DO_NOTHING, db_column='ID_libro')  # FK al PK de Libro
    isbn = models.CharField(db_column='ISBN', max_length=20)  # simple CharField

    class Meta:
        managed = False
        db_table = 'Venta'
        unique_together = (('id_libro', 'isbn'),)


class ClubLecturaLibro(models.Model):
    id_club = models.OneToOneField(ClubLectura, models.DO_NOTHING, db_column='ID_club', primary_key=True)  # Field name made lowercase. The composite primary key (ID_club, ID_libro, ISBN) found, that is not supported. The first column is selected.
    id_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='ID_libro')  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=20)

    class Meta:
        managed = False
        db_table = 'club_lectura_libro'
        unique_together = (('id_club', 'id_libro', 'isbn'),)


class UsuarioClub(models.Model):
    id_usuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='ID_usuario', primary_key=True)  # Field name made lowercase. The composite primary key (ID_usuario, ID_club) found, that is not supported. The first column is selected.
    id_club = models.ForeignKey(ClubLectura, models.DO_NOTHING, db_column='ID_club')  # Field name made lowercase.
    fecha_union = models.DateField()

    class Meta:
        managed = False
        db_table = 'usuario_club'
        unique_together = (('id_usuario', 'id_club'),)
