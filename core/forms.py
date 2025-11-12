# core/forms.py
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'titulo', 'autor', 'anio_publicacion', 'genero', 'modalidad', 'resumen']
