from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'clients$', views.get_clients),
    url(r'vehicles$', views.vehicle_view),
    url(r'usecontrol_add$', views.usecontrol_add),
    url(r'usecontrol_list$', views.usecontrol_list),
    url(r'$', views.index),
]
