# core/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Libro

def home(request):
    return render(request, 'core/home.html')


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
            qs = qs.filter(
                Q(titulo__icontains=q) |
                Q(autor__icontains=q) |
                Q(isbn__icontains=q)
            )
        return qs


class LibroDetail(DetailView):
    model = Libro
    template_name = 'core/libro_detail.html'
    context_object_name = 'libro'


# ✅ Require login to create, update, delete
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
