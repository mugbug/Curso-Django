from django.shortcuts import render
from django.http import HttpResponse
from resources.models import Vehicle, Driver, UseControl

class Veiculo(object):
    name = None

def index(request):
    v1 = Veiculo()
    v1.name = "Fusca Bala"

    v2 = Veiculo()
    v2.name = 2007

    v3 = Veiculo()
    v3.name = None

    var_dict = {
        'lista_veiculos': [v1, v2, v3]
    }

    return render(request, 'hello.html', var_dict)

def get_clients(request):
    var_dict = {
        'list_client': ['Leandro', 'Ellen', 'Eloise']
    }
    return render(request, 'clients.html', var_dict)

def vehicle_view(request):
    return render(request, 'vehicle.html')

def usecontrol_add(request):
    driver = Driver()
    driver.name = 'Pedro'
    driver.save()

    vehicle = Vehicle()
    vehicle.name = 'Palio'
    vehicle.license_plate = 'ABC1234'
    vehicle.save()

    usecontrol = UseControl()
    usecontrol.driver = driver
    usecontrol.vehicle = vehicle
    usecontrol.save()
    
    return render(request, 'usecontrol_list.html')

def usecontrol_list(request):
    usecontrol = UseControl.objects.all()[0]
    data = {
        'vehicle': usecontrol.vehicle.name,
        'driver': usecontrol.driver.name,
        'date_started': usecontrol.date_started,
    }
    return render(request, 'usecontrol_list.html', data)
