from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('getPlatos',views.getPlatos),
    path('getAlimentos',views.getAlimentos),
    path('postPlato',views.postPlato),
    path('postAlimento',views.postAlimento),
    path('getPlato/<id>',views.getPlato),
    path('getAlimento/<id>',views.getAlimento),
    path('deleteAlimento/<id>',views.deleteAlimento),
    path('deletePlato/<id>',views.deletePlato)
    ]