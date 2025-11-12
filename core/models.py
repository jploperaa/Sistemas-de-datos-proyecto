# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Catalogo(models.Model):
    id_catalogo = models.AutoField(db_column='ID_catalogo', primary_key=True)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateField(db_column='fecha_creacion', blank=True, null=True)

    class Meta:
        managed = False          # ¡Importante! La tabla ya existe en MySQL.
        db_table = 'Catalogo'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


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
    def usuario_nombre(self):
        # Ajusta al campo correcto del modelo Usuario (nombre, correo, etc.)
        return getattr(self.id_usuario, "nombre", str(self.id_usuario))

    def libro_titulo(self):
        # Ajusta al campo correcto del modelo Libro (titulo, etc.)
        return getattr(self.id_libro, "titulo", str(self.id_libro))

    usuario_nombre.short_description = "Usuario"
    libro_titulo.short_description = "Libro"


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




# core/models.py

class Resea(models.Model):
    id_reseña = models.AutoField(primary_key=True)
    calificacion = models.IntegerField()
    fecha_reseña = models.DateField()
    id_libro = models.ForeignKey('Libro', on_delete=models.CASCADE, db_column='ID_libro')
    isbn = models.CharField(max_length=20)
    id_usuario_autor = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='ID_usuario_autor')
    contenido = models.TextField(db_column='contenido')  # ajusta el nombre si tu columna se llama distinto


    # readable columns for your list
    def usuario_nombre(self):
        return getattr(self.id_usuario_autor, "nombre", str(self.id_usuario_autor))

    def libro_titulo(self):
        return getattr(self.id_libro, "titulo", str(self.id_libro))
    def contenido_resumen(self):
        txt = self.contenido or ""
        return txt[:80] + ("…" if len(txt) > 80 else "")
    contenido_resumen.short_description = "Contenido"

    usuario_nombre.short_description = "Usuario Autor"
    libro_titulo.short_description = "Libro"

    class Meta:
        db_table = 'Reseña'   # <-- EXACT table name in MySQL (accent included)
        managed = False       # Django won’t try to create/alter this table
        ordering = ['-fecha_reseña']  # avoid the pagination warning









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
    id_venta = models.IntegerField(primary_key=True)
    fecha_venta = models.DateField()
    estado = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='ID_usuario')
    id_libro   = models.ForeignKey('Libro', on_delete=models.CASCADE, db_column='ID_libro')
    isbn       = models.CharField(max_length=20)

    # Helpers para mostrar nombres en la tabla
    def usuario_nombre(self):
        return self.id_usuario.nombre if self.id_usuario else ""
    def libro_titulo(self):
        return self.id_libro.titulo if self.id_libro else ""

    class Meta:
        db_table = 'Venta'   # <- nombre EXACTO de la tabla en MySQL
        managed = False      # <- Django no crea/alterará esta tabla
        ordering = ['fecha_venta']  # evita el warning de “unordered”




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
