from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField()
    vin_code = models.CharField()
    client_name = models.CharField()

    def __str__(self):
        return f'{self.make} {self.model} {self.license_plate} {self.vin_code}'