from datetime import date

from django.test import TestCase

from .models import Vehicle, Driver, UseControl, ManagerControl
# Create your tests here.

class VehicleTest(TestCase):

    def setUp(self):
        date_manufacture = date(2007, 1, 2)
        self.vehicle = Vehicle.objects.create(name='Uno', license_plate='HFW4562', \
                                            manufacture_year=date_manufacture)
    # sempre começar com test_
    def test_models(self):
        self.assertTrue(self.vehicle.is_active) #verifica se tá ativo
        self.assertEqual(self.vehicle.usecontrols.count(), 0) #0: expected value

class UseControlTest(TestCase):

    def setUp(self):
        driver = Driver()
        driver.name = 'Pedro'
        driver.save()

        vehicle = Vehicle()
        vehicle.name = 'Palio'
        vehicle.license_plate = 'ABC1234'
        vehicle.save()

        self.usecontrol = UseControl()
        self.usecontrol.driver = driver
        self.usecontrol.vehicle = vehicle
        self.usecontrol.save()

    def test_date_attributes_are_valid(self):
        self.assertNotEqual(self.usecontrol.date_started, None)
        self.assertEqual(self.usecontrol.date_ended, None)


class VehicleViewTests(TestCase):

    def test_vehicle_list(self):
        response = self.client.get('/resources/vehicles')
        self.assertEqual(response.status_code, 200)

    def test_must_create_vehicle(self):
        data = {
            'name': 'Fiat Palio',
            'description': 'Modelo Popular',
            'description': 'GRS2577',
            'license_plate': '2008-01-01',
        }
        response = self.client.post('/resources/vehicle/add', data)
        # Check status code for redirect
        self.assertEqual(response.status_code, 200)
        vehicle_db = Vehicle.objects.all().first()
        self.assertEqual(vehicle_db.id, 1) # TODO: AttributeError: 'NoneType' object has no attribute 'id'
        self.assertEqual(vehicle_db.name, data.get('name'))


class ManagerControlModelTest(TestCase):
    fixtures = ['manager_fixture']

    def test_manager_control_relations(self):
        man_ctrl = ManagerControl.objects.all().first()
        self.assertEqual(man_ctrl.user.id, 1)
        self.assertEqual(man_ctrl.user.username, 'joao')
