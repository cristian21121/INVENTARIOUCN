from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def autenticacion(request):
    return render(request, 'autenticacion.html')
