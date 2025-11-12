# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # -------- Libros
    path('libros/', views.LibroList.as_view(), name='libro_list'),
    path('libros/nuevo/', views.LibroCreate.as_view(), name='libro_create'),
    path('libros/<int:pk>/', views.LibroDetail.as_view(), name='libro_detail'),
    path('libros/<int:pk>/editar/', views.LibroUpdate.as_view(), name='libro_update'),
    path('libros/<int:pk>/eliminar/', views.LibroDelete.as_view(), name='libro_delete'),

    # -------- Catálogos
    path('catalogos/', views.CatalogoList.as_view(), name='catalogo_list'),
    path('catalogos/nuevo/', views.CatalogoCreate.as_view(), name='catalogo_create'),
    path('catalogos/<int:pk>/', views.CatalogoDetail.as_view(), name='catalogo_detail'),
    path('catalogos/<int:pk>/editar/', views.CatalogoUpdate.as_view(), name='catalogo_update'),
    path('catalogos/<int:pk>/eliminar/', views.CatalogoDelete.as_view(), name='catalogo_delete'),

    # -------- Clubes de lectura
    path('clubes/', views.ClubList.as_view(), name='club_list'),
    path('clubes/nuevo/', views.ClubCreate.as_view(), name='club_create'),
    path('clubes/<int:pk>/', views.ClubDetail.as_view(), name='club_detail'),
    path('clubes/<int:pk>/editar/', views.ClubUpdate.as_view(), name='club_update'),
    path('clubes/<int:pk>/eliminar/', views.ClubDelete.as_view(), name='club_delete'),

    # -------- Publicaciones
    path('publicaciones/', views.PublicacionList.as_view(), name='publicacion_list'),
    path('publicaciones/nuevo/', views.PublicacionCreate.as_view(), name='publicacion_create'),
    path('publicaciones/<int:pk>/', views.PublicacionDetail.as_view(), name='publicacion_detail'),
    path('publicaciones/<int:pk>/editar/', views.PublicacionUpdate.as_view(), name='publicacion_update'),
    path('publicaciones/<int:pk>/eliminar/', views.PublicacionDelete.as_view(), name='publicacion_delete'),

    # -------- Intercambios
    path('intercambios/', views.IntercambioList.as_view(), name='intercambio_list'),
    path('intercambios/nuevo/', views.IntercambioCreate.as_view(), name='intercambio_create'),
    path('intercambios/<int:pk>/', views.IntercambioDetail.as_view(), name='intercambio_detail'),
    path('intercambios/<int:pk>/editar/', views.IntercambioUpdate.as_view(), name='intercambio_update'),
    path('intercambios/<int:pk>/eliminar/', views.IntercambioDelete.as_view(), name='intercambio_delete'),

    # -------- Reseñas
    path('resenas/', views.ResenaList.as_view(), name='resena_list'),
    path('resenas/nuevo/', views.ResenaCreate.as_view(), name='resena_create'),
    path('resenas/<int:pk>/', views.ResenaDetail.as_view(), name='resena_detail'),
    path('resenas/<int:pk>/editar/', views.ResenaUpdate.as_view(), name='resena_update'),
    path('resenas/<int:pk>/eliminar/', views.ResenaDelete.as_view(), name='resena_delete'),

    # -------- Ventas
    path('ventas/', views.VentaList.as_view(), name='venta_list'),
    path('ventas/nuevo/', views.VentaCreate.as_view(), name='venta_create'),
    path('ventas/<int:pk>/', views.VentaDetail.as_view(), name='venta_detail'),
    path('ventas/<int:pk>/editar/', views.VentaUpdate.as_view(), name='venta_update'),
    path('ventas/<int:pk>/eliminar/', views.VentaDelete.as_view(), name='venta_delete'),

    # -------- Usuarios (negocio)
    path('usuarios-negocio/', views.UsuarioList.as_view(), name='usuario_list'),
    path('usuarios-negocio/nuevo/', views.UsuarioCreate.as_view(), name='usuario_create'),
    path('usuarios-negocio/<int:pk>/', views.UsuarioDetail.as_view(), name='usuario_detail'),
    path('usuarios-negocio/<int:pk>/editar/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('usuarios-negocio/<int:pk>/eliminar/', views.UsuarioDelete.as_view(), name='usuario_delete'),

    # -------- Tablas puente
    path('usuario-club/', views.UsuarioClubList.as_view(), name='usuarioclub_list'),
    path('usuario-club/nuevo/', views.UsuarioClubCreate.as_view(), name='usuarioclub_create'),
    path('usuario-club/<int:pk>/', views.UsuarioClubDetail.as_view(), name='usuarioclub_detail'),
    path('usuario-club/<int:pk>/editar/', views.UsuarioClubUpdate.as_view(), name='usuarioclub_update'),
    path('usuario-club/<int:pk>/eliminar/', views.UsuarioClubDelete.as_view(), name='usuarioclub_delete'),

    path('club-libro/', views.ClubLecturaLibroList.as_view(), name='clublecturalibro_list'),
    path('club-libro/nuevo/', views.ClubLecturaLibroCreate.as_view(), name='clublecturalibro_create'),
    path('club-libro/<int:pk>/', views.ClubLecturaLibroDetail.as_view(), name='clublecturalibro_detail'),
    path('club-libro/<int:pk>/editar/', views.ClubLecturaLibroUpdate.as_view(), name='clublecturalibro_update'),
    path('club-libro/<int:pk>/eliminar/', views.ClubLecturaLibroDelete.as_view(), name='clublecturalibro_delete'),
]
