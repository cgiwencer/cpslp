from Aplicaciones import Usuarios
from django.shortcuts import render, redirect
from .models import usuario

# Create your views here.
def home(request):
    users=usuario.objects.all()
    return render(request,"gestionUsuarios.html",{"usuarios": users})

def registrarUsuario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    usua=request.POST['txtUsuario']
    clave=request.POST['txtClave']

    graba = usuario.objects.create(codigo=codigo, nombre=nombre, nomusu=usua, clave=clave)
    return redirect('/')

def edicionUsuario(request, codigo):
    user=usuario.objects.get(codigo = codigo)
    return render(request, "edicionUsuario.html", {"usuario": user})

def editarUsuario(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    usua=request.POST['txtUsuario']
    clave=request.POST['txtClave']

    user = usuario.objects.get(codigo = codigo)
    user.nombre = nombre
    user.usua = usua
    user.clave = clave
    user.save()

    return redirect('/')

def eliminarUsuario(request, codigo):
    user=usuario.objects.get(codigo=codigo)
    user.delete()

    return redirect('/')

def login(request):
    return render(request, "login.html")