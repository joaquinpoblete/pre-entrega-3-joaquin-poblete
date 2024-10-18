from django.shortcuts import render, redirect
from .models import Autor, Libro, Reseña
from .forms import AutorForm, LibroForm, ReseñaForm, BuscarLibroForm

def inicio(request):
    return render(request, 'base.html')

def insertar_datos(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroForm()
    return render(request, 'insertar.html', {'form': form})

def buscar_libro(request):
    form = BuscarLibroForm()
    libros = None
    if request.method == 'POST':
        form = BuscarLibroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            libros = Libro.objects.filter(titulo__icontains=titulo)
    return render(request, 'buscar_libro.html', {'form': form, 'libros': libros})
