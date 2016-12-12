from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'clients$', get_clients),
    # list vehicles
    url(r'vehicles$', VehicleListView.as_view(), name='vehicle_list'),
    url(r'usecontrol_add$', usecontrol_add),
    url(r'usecontrol_list$', UseControlView.as_view()),
    # redirect views
    url(r'validate_vehicle/(?P<pk>\d+)$', VehicleRedirectView.as_view(), \
                                                name='vehicle_counter'),
    url(r'vehicle_detail/(?P<pk>\d+)/$', VehicleDetailView.as_view(), \
                                                name='vehicle_detail'),
    # edit views
    url(r'vehicle/add$', VehicleCreate.as_view(), name='vehicle_add'),
    url(r'vehicle/(?P<pk>\d+)$', VehicleUpdate.as_view(), \
                                                name='vehicle_update'),
    url(r'vehicle/(?P<pk>\d+)/delete$', VehicleDelete.as_view(), \
                                                name='vehicle_delete'),
    # default page for resources
    url(r'$', index, name='resources_default'),
]
