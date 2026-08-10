from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField()
    vin_code = models.CharField()
    client_name = models.CharField()

    def __str__(self):
        return f"{self.make} {self.model}"

class Order(models.Model):
    car = models.ForeignKey(to="Car",
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car} ({self.date})'


class Order_line(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE)
    service = models.ForeignKey(to="Service",
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f' {self.service} - {self.quantity}'
