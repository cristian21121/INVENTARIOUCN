from datetime import datetime
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from inventarioucn.models import Equipos, Reserva, Soportes

def inicio(request):
    #Reservas y equipos de las reservas
    try:
        reservas = Reserva.objects.get(IdUsuario = request.user)
        equipos = reservas.IdEquipo
    except:
        reservas = ()
        equipos = ()
    
    #Soportes y equipos de los soportes
    try:
        soportes = Soportes.objects.get(IdUsuario = request.user)
        equiposSoporte = soportes.IdEquipo
    except:
        soportes = ()
        equiposSoporte = ()

    return render(request, 'inicio.html', {
        'equipos': equipos,
        'reservas': reservas,
        'soportes': soportes,
        'equipoSoporte': equiposSoporte
    })

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password1'],
                    first_name = request.POST['firstName'],
                    last_name = request.POST['lastName'],
                    email = request.POST['email']
                )
                user.save()
                login(request, user)
                return redirect('gestion')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                    })

def gestion(request):
    if request.method == 'GET':
        equipos = Equipos.objects.all()
        return render(request, 'gestion.html', {'equipos': equipos})
    else:
        Equipo = request.POST['IdEquipo'] #Revisar si esta linea sirve
        equipo = Equipos.objects.get(IdEquipo = Equipo)
        date = datetime.now()
        reserva = Reserva (
            IdEquipo = equipo,
            IdUsuario = request.user,
            Detalle = request.POST['Detalle'],
            FechaInicio = date.strftime("%Y-%d-%m %H:%M:%S")
        )
        reserva.save()
        return redirect('inicio')

def signout(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )

        if user is None:
            return render(request, 'signin.html', {
                'error': 'Usuario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('gestion')

def soporte(request):
    if request.method == 'GET':
        return render(request, 'soporte.html')
    else:
        Equipo = request.POST['IdEquipo']
        equipo = Equipos.objects.get(IdEquipo = Equipo)
        date = datetime.now()
        soporte = Soportes(
            FechaInicio = date.strftime("%Y-%d-%m %H:%M:%S"),
            IdEquipo = equipo,
            IdUsuario = request.user,
            Detalle = request.POST['Detalle']
        )
        soporte.save()
        return redirect('inicio')