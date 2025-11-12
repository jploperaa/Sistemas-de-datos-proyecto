# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LibroList.as_view(), name='libro_list'),
    path('libro/<int:pk>/', views.LibroDetail.as_view(), name='libro_detail'),
    path('libro/nuevo/', views.LibroCreate.as_view(), name='libro_create'),
    path('libro/<int:pk>/editar/', views.LibroUpdate.as_view(), name='libro_update'),
    path('libro/<int:pk>/eliminar/', views.LibroDelete.as_view(), name='libro_delete'),
]
