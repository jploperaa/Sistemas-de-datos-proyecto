# core/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import (
    Libro, Catalogo, ClubLectura, Publicacion, Intercambio,
    Resea, Venta, Usuario, UsuarioClub, ClubLecturaLibro
)

def home(request):
    return render(request, 'core/home.html')

# =============== LIBRO (tuviste esto antes) ===============
class LibroList(ListView):
    model = Libro
    template_name = 'core/libro_list.html'
    context_object_name = 'libros'
    paginate_by = 10
    ordering = ['titulo']

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(titulo__icontains=q) | Q(autor__icontains=q) | Q(isbn__icontains=q))
        return qs

class LibroDetail(DetailView):
    model = Libro
    template_name = 'core/libro_detail.html'
    context_object_name = 'libro'

class LibroCreate(LoginRequiredMixin, CreateView):
    model = Libro
    fields = ['isbn', 'titulo', 'autor', 'anio_publicacion', 'genero', 'modalidad', 'resumen']
    template_name = 'core/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    fields = ['isbn', 'titulo', 'autor', 'anio_publicacion', 'genero', 'modalidad', 'resumen']
    template_name = 'core/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = 'core/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')


# =========== Generic helpers for other models ===========
class GenericList(ListView):
    template_name = 'core/generic_list.html'
    context_object_name = 'objects'
    paginate_by = 12
    ordering = None
    list_display = []  # fields to show as columns
    title = ''         # page title
    create_url_name = ''  # url name to create

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['list_display'] = self.list_display
        ctx['create_url_name'] = self.create_url_name
        ctx['model_name'] = self.model._meta.verbose_name.title() if self.model._meta.verbose_name else self.model.__name__
        return ctx

class GenericDetail(DetailView):
    template_name = 'core/generic_detail.html'
    context_object_name = 'obj'
    title = ''

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['fields'] = [f.name for f in self.model._meta.fields]
        return ctx

class GenericCreate(LoginRequiredMixin, CreateView):
    template_name = 'core/generic_form.html'
    success_url = None
    title = ''
    fields = '__all__'   # override per view if needed

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        return ctx

class GenericUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'core/generic_form.html'
    success_url = None
    title = ''
    fields = '__all__'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        return ctx

class GenericDelete(LoginRequiredMixin, DeleteView):
    template_name = 'core/generic_confirm_delete.html'
    success_url = None
    title = ''

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        return ctx


# ===================== CATÁLOGO =====================
class CatalogoList(GenericList):
    model = Catalogo
    title = 'Catálogos'
    list_display = ['nombre', 'fecha_creacion']
    create_url_name = 'catalogo_create'

class CatalogoDetail(GenericDetail):
    model = Catalogo
    title = 'Detalle de Catálogo'

class CatalogoCreate(GenericCreate):
    model = Catalogo
    fields = ['nombre', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('catalogo_list')
    title = 'Crear Catálogo'

class CatalogoUpdate(GenericUpdate):
    model = Catalogo
    fields = ['nombre', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('catalogo_list')
    title = 'Editar Catálogo'

class CatalogoDelete(GenericDelete):
    model = Catalogo
    success_url = reverse_lazy('catalogo_list')
    title = 'Eliminar Catálogo'


# =================== CLUB LECTURA ===================
class ClubList(GenericList):
    model = ClubLectura
    title = 'Clubes de Lectura'
    list_display = ['nombre', 'estado', 'fecha_creacion']
    create_url_name = 'club_create'

class ClubDetail(GenericDetail):
    model = ClubLectura
    title = 'Detalle de Club'

class ClubCreate(GenericCreate):
    model = ClubLectura
    fields = ['nombre', 'descripcion', 'estado', 'fecha_creacion']
    success_url = reverse_lazy('club_list')
    title = 'Crear Club'

class ClubUpdate(GenericUpdate):
    model = ClubLectura
    fields = ['nombre', 'descripcion', 'estado', 'fecha_creacion']
    success_url = reverse_lazy('club_list')
    title = 'Editar Club'

class ClubDelete(GenericDelete):
    model = ClubLectura
    success_url = reverse_lazy('club_list')
    title = 'Eliminar Club'


# =================== PUBLICACIÓN ===================
class PublicacionList(GenericList):
    model = Publicacion
    title = 'Publicaciones'
    list_display = ['modalidad', 'estado', 'precio', 'fecha_publicacion']
    create_url_name = 'publicacion_create'

class PublicacionDetail(GenericDetail):
    model = Publicacion
    title = 'Detalle de Publicación'

class PublicacionCreate(GenericCreate):
    model = Publicacion
    fields = ['modalidad','estado','fecha_publicacion','precio','id_usuario','id_catalogo','id_libro','isbn']
    success_url = reverse_lazy('publicacion_list')
    title = 'Crear Publicación'

class PublicacionUpdate(GenericUpdate):
    model = Publicacion
    fields = ['modalidad','estado','fecha_publicacion','precio','id_usuario','id_catalogo','id_libro','isbn']
    success_url = reverse_lazy('publicacion_list')
    title = 'Editar Publicación'

class PublicacionDelete(GenericDelete):
    model = Publicacion
    success_url = reverse_lazy('publicacion_list')
    title = 'Eliminar Publicación'


# =================== INTERCAMBIO ===================
class IntercambioList(GenericList):
    model = Intercambio
    title = 'Intercambios'
   
    list_display = ['fecha', 'estado', 'usuario_nombre', 'libro_titulo', 'isbn']
    create_url_name = 'intercambio_create'

    def get_queryset(self):
        # para evitar N+1 queries al resolver los nombres
        return super().get_queryset().select_related('id_usuario', 'id_libro')


class IntercambioDetail(GenericDetail):
    model = Intercambio
    title = 'Detalle de Intercambio'

class IntercambioCreate(GenericCreate):
    model = Intercambio
    fields = ['fecha','estado','id_usuario','id_libro','isbn']
    success_url = reverse_lazy('intercambio_list')
    title = 'Crear Intercambio'

class IntercambioUpdate(GenericUpdate):
    model = Intercambio
    fields = ['fecha','estado','id_usuario','id_libro','isbn']
    success_url = reverse_lazy('intercambio_list')
    title = 'Editar Intercambio'

class IntercambioDelete(GenericDelete):
    model = Intercambio
    success_url = reverse_lazy('intercambio_list')
    title = 'Eliminar Intercambio'


# ====================== RESEÑA ======================
class ResenaList(GenericList):
    model = Resea
    title = 'Reseñas'
    list_display = ['calificacion', 'fecha_reseña', 'libro_titulo', 'isbn', 'usuario_nombre','contenido_resumen']
    create_url_name = 'reseña_create'

    def get_queryset(self):
        return super().get_queryset().select_related('id_libro', 'id_usuario_autor')

class ResenaDetail(GenericDetail):
    model = Resea
    title = 'Detalle de Reseña'

class ResenaCreate(GenericCreate):
    model = Resea
    fields = ['calificacion','contenido','fecha_reseña','id_usuario_autor','id_usuario_comenta','id_libro','isbn']
    success_url = reverse_lazy('resena_list')
    title = 'Crear Reseña'

class ResenaUpdate(GenericUpdate):
    model = Resea
    fields = ['calificacion','contenido','fecha_reseña','id_usuario_autor','id_usuario_comenta','id_libro','isbn']
    success_url = reverse_lazy('resena_list')
    title = 'Editar Reseña'

class ResenaDelete(GenericDelete):
    model = Resea
    success_url = reverse_lazy('resena_list')
    title = 'Eliminar Reseña'


# ======================= VENTA ======================
class VentaList(GenericList):
    model = Venta
    title = 'Ventas'
    list_display = ['fecha_venta','estado','precio',
                    'usuario_nombre','libro_titulo','isbn']   # <- aquí

    def get_queryset(self):
        
        return super().get_queryset().select_related('id_usuario', 'id_libro')


class VentaDetail(GenericDetail):
    model = Venta
    title = 'Detalle de Venta'

class VentaCreate(GenericCreate):
    model = Venta
    # id_venta es PK manual en tu tabla -> hay que editarlo por formulario
    fields = ['id_venta','fecha_venta','estado','precio','id_usuario','id_libro','isbn']
    success_url = reverse_lazy('venta_list')
    title = 'Crear Venta'

class VentaUpdate(GenericUpdate):
    model = Venta
    fields = ['fecha_venta','estado','precio','id_usuario','id_libro','isbn']
    success_url = reverse_lazy('venta_list')
    title = 'Editar Venta'

class VentaDelete(GenericDelete):
    model = Venta
    success_url = reverse_lazy('venta_list')
    title = 'Eliminar Venta'


# ====================== USUARIO =====================
class UsuarioList(GenericList):
    model = Usuario
    title = 'Usuarios (negocio)'
    list_display = ['nombre','correo','telefono','ciudad']
    create_url_name = 'usuario_create'

class UsuarioDetail(GenericDetail):
    model = Usuario
    title = 'Detalle de Usuario (negocio)'

class UsuarioCreate(GenericCreate):
    model = Usuario
    fields = ['nombre','correo','telefono','password','ciudad']
    success_url = reverse_lazy('usuario_list')
    title = 'Crear Usuario (negocio)'

class UsuarioUpdate(GenericUpdate):
    model = Usuario
    fields = ['nombre','correo','telefono','password','ciudad']
    success_url = reverse_lazy('usuario_list')
    title = 'Editar Usuario (negocio)'

class UsuarioDelete(GenericDelete):
    model = Usuario
    success_url = reverse_lazy('usuario_list')
    title = 'Eliminar Usuario (negocio)'


# ================ TABLAS PUENTE =====================
class UsuarioClubList(GenericList):
    model = UsuarioClub
    title = 'Unión Usuario–Club'
    list_display = ['id_usuario','id_club','fecha_union']
    create_url_name = 'usuarioclub_create'

class UsuarioClubDetail(GenericDetail):
    model = UsuarioClub
    title = 'Detalle Usuario–Club'

class UsuarioClubCreate(GenericCreate):
    model = UsuarioClub
    fields = ['id_usuario','id_club','fecha_union']
    success_url = reverse_lazy('usuarioclub_list')
    title = 'Crear Usuario–Club'

class UsuarioClubUpdate(GenericUpdate):
    model = UsuarioClub
    fields = ['id_usuario','id_club','fecha_union']
    success_url = reverse_lazy('usuarioclub_list')
    title = 'Editar Usuario–Club'

class UsuarioClubDelete(GenericDelete):
    model = UsuarioClub
    success_url = reverse_lazy('usuarioclub_list')
    title = 'Eliminar Usuario–Club'


class ClubLecturaLibroList(GenericList):
    model = ClubLecturaLibro
    title = 'Unión Club–Libro'
    list_display = ['id_club','id_libro','isbn']
    create_url_name = 'clublecturalibro_create'

class ClubLecturaLibroDetail(GenericDetail):
    model = ClubLecturaLibro
    title = 'Detalle Club–Libro'

class ClubLecturaLibroCreate(GenericCreate):
    model = ClubLecturaLibro
    fields = ['id_club','id_libro','isbn']
    success_url = reverse_lazy('clublecturalibro_list')
    title = 'Crear Club–Libro'

class ClubLecturaLibroUpdate(GenericUpdate):
    model = ClubLecturaLibro
    fields = ['id_club','id_libro','isbn']
    success_url = reverse_lazy('clublecturalibro_list')
    title = 'Editar Club–Libro'

class ClubLecturaLibroDelete(GenericDelete):
    model = ClubLecturaLibro
    success_url = reverse_lazy('clublecturalibro_list')
    title = 'Eliminar Club–Libro'
