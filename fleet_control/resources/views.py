from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import DetailView, ListView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

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

# def usecontrol_list(request):
#     usecontrol = UseControl.objects.all()[0]
#     data = {
#         'vehicle': usecontrol.vehicle.name,
#         'driver': usecontrol.driver.name,
#         'date_started': usecontrol.date_started,
#     }
#     return render(request, 'usecontrol_list.html', data)


class UseControlView(TemplateView):
    template_name = 'usecontrol_list.html'

    def get_context_data(self, **kwargs):
        context = super(UseControlView, self).get_context_data(**kwargs)
        usecontrol = UseControl.objects.all().first()
        # import ipdb; ipdb.set_trace()
        context['vehicle'] = usecontrol.vehicle.name
        context['driver'] = usecontrol.driver.name
        context['date_started'] = usecontrol.date_started
        return context


class VehicleRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'vehicle_detail'

    # import ipdb; ipdb.set_trace()
    def get_redirect_url(self, *args, **kwargs):
        vehicle = get_object_or_404(Vehicle, pk=kwargs['pk'])
        return super(VehicleRedirectView, self).get_redirect_url(*args, **kwargs)


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'


class VehicleCreate(CreateView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')
    template_name = 'vehicle_form.html'
    fields = ['name', 'description', 'license_plate', 'vendor']


class VehicleUpdate(UpdateView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')
    template_name = 'vehicle_form.html'
    fields = ['name', 'description', 'license_plate', 'vendor']


class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')
    template_name = 'vehicle_confirm_delete.html'


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    queryset = Vehicle.objects.order_by('name')
    context_object_name = 'vehicle_list'
    paginate_by = 4
