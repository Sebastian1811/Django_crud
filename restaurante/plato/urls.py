from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('platos/',views.platos),
    path('registrarPlato/',views.registrarPlato),
    path('alimentos/',views.ingredientes),
    path('registrarIngrediente/',views.registrarAlimento),
    path('edicionPlato/<codigo>',views.edicionPlato),
    path('editarPlato/',views.editarPlato),
    path('eliminarPlato/<codigo>',views.eliminarPlato),
    path('edicionAlimento/<codigo>',views.edicionAlimento),
    path('eliminarAlimento/<codigo>',views.eliminarAlimiento),
    path('editarAlimento/',views.editarAlimento)
]