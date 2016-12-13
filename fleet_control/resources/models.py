from django.db import models
from datetime import date
from django.conf import settings
# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=128)


class UseControl(models.Model):
    driver = models.ForeignKey('Driver')
    vehicle = models.ForeignKey('Vehicle')
    date_started = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(blank=True, null=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=30) # verbose_name: label no admin
    description = models.TextField(null=True, blank=True)
    vendor = models.IntegerField(null=True)
    license_plate = models.CharField(max_length=7, default='')
    manufacture_year = models.DateField(default=date.today())
    is_active = models.BooleanField(default=True)

    manufacturer = models.ForeignKey('Manufacturer', null=True)
    usecontrols = models.ManyToManyField(Driver, through='UseControl')

    # just like toString
    def __str__(self):
        # return self.name
        return '{0} - {1}'.format(self.name, self.license_plate)

class ManagerControl(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    name = models.CharField(max_length=30)
