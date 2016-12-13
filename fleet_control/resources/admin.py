from django.contrib import admin

from .models import ManagerControl, Manufacturer, \
                Vehicle, Driver, UseControl

admin.site.register(ManagerControl)
admin.site.register(Manufacturer)
admin.site.register(Vehicle)
admin.site.register(Driver)
admin.site.register(UseControl)
