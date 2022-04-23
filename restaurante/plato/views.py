from mailbox import NoSuchMailboxError
from sre_constants import CATEGORY_UNI_SPACE
from django.shortcuts import redirect, render
from . models import Alimento, Plato
# Create your views here.
def home(request):
    return redirect('/platos')

def platos(request):
    platos = Plato.objects.all()
    ingredientes = Alimento.objects.all()
    return render(request,"gestionPlatos.html",{"platos":platos,"alimentos":ingredientes})

def ingredientes(request):
    ingredientes = Alimento.objects.all()
    return render(request,"gestionIngredientes.html",{"alimentos":ingredientes})

def registrarAlimento(request):
    id = request.POST['txtid']
    nombre = request.POST['txtnombre']
    categoria = request.POST['txtcategoria']
    Alimento.objects.create(id=id,nombre=nombre,categoria=categoria)
    return redirect('/alimentos')

def registrarPlato(request):
    alimento = Alimento.objects.get(id =request.POST['id-ingrediente'])
    id = request.POST['txtid']
    nombre = request.POST['txtnombre']
    tiempo = request.POST['tiempoP']
    categoria = request.POST['txtcategoria']
    ingredientes = alimento
    plato = Plato.objects.create(id =id,nombre=nombre,tiempo_preparaciona=tiempo,categoria=categoria,ingredientes=ingredientes)
    return redirect('/platos')

def editarPlato(request):
    alimento = Alimento.objects.get(id =request.POST['id-ingrediente'])
    id = request.POST['txtid']
    nombre = request.POST['txtnombre']
    tiempo = request.POST['tiempoP']
    categoria = request.POST['txtcategoria']
    ingredientes = alimento

    plato = Plato.objects.get(id=id)
    plato.id = id
    plato.nombre = nombre
    plato.tiempo_preparaciona = tiempo
    plato.categoria = categoria
    plato.ingredientes = ingredientes
    plato.save()
    return redirect('/platos')

def edicionPlato(request,codigo):
    plato = Plato.objects.get(id=codigo)
    ingredientes = Alimento.objects.all()
    return render(request,"editarPlato.html",{"plato":plato,"alimentos":ingredientes})
    

def eliminarPlato(request,codigo):
    plato = Plato.objects.get(id=codigo)
    plato.delete()
    return redirect('/platos')
    

def edicionAlimento(request,codigo):
    alimento = Alimento.objects.get(id=codigo)
    return render(request,"editarAlimento.html",{"alimento":alimento})

def editarAlimento(request):
    id = request.POST['txtid']
    nombre = request.POST['txtnombre']
    categoria = request.POST['txtcategoria']
    alimento = Alimento.objects.get(id=id)
    alimento.id = id
    alimento.nombre = nombre
    alimento.categoria = categoria
    alimento.save()
    return redirect('/alimentos')
    

def eliminarAlimiento(request,codigo):
    alimento = Alimento.objects.get(id=codigo)
    alimento.delete()
    return redirect('/alimentos')

    
