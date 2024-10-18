from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('insertar/', views.insertar_datos, name='insertar'),
    path('buscar/', views.buscar_libro, name='buscar'),
]