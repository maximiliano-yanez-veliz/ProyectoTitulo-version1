from django.urls import path
from PlanillaEjercicios.views import EjercicioListView, eliminar_ejercicio

urlpatterns = [
    path('', EjercicioListView.as_view(), name='gestion_ejercicios'),
    path('eliminacionEjercicios/<int:id>', eliminar_ejercicio)
]

