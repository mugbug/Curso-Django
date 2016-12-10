from django import template
from resources.models import Vehicle
from datetime import date

register = template.Library()

@register.simple_tag
def get_vehicle(num_items):
    lista = []
    v1 = Vehicle()
    v1.name = 'Uno'
    v1.description = 'Carro da Fiat'
    v1.license_plate = 'HKF3654'
    v1.manufacture_year = date(2007, 1, 1)
    v1.save()
    lista.append(v1)
    # lista.append('Fiat')
    # lista.append('KIA')
    # lista.append('Volks')
    # lista.append('Ford')
    # lista.append('Toyota')

    return lista[:num_items]
