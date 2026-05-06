from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),

    # TIPOS
    path('tipos/', views.lista_tipos, name='lista_tipos'),
    path('tipos/crear/', views.crear_tipo, name='crear_tipo'),
    path('tipos/editar/<int:id>/', views.editar_tipo, name='editar_tipo'),
    path('tipos/eliminar/<int:id>/', views.eliminar_tipo, name='eliminar_tipo'),

    # VEHICULOS
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('vehiculos/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    
]