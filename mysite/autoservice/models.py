from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Service(models.Model):
    name = models.CharField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField(max_length=10)
    vin_code = models.CharField(max_length=16)
    client_name = models.CharField()
    cover = models.ImageField(upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model}"

class Order(models.Model):
    car = models.ForeignKey(to="Car",
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True,
                            related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    car_owner = models.ForeignKey(to=User, verbose_name="Car_owner", on_delete=models.SET_NULL, null=True, blank=True)
    due_back = models.DateField(null=True, blank=True)

    ORDER_STATUS = (
        ('p' , 'Patvirtinta'),
        ('v' , 'Vykdoma'),
        ('a' , 'Atšaukta'),
        ('į' , 'Įvykdyta'),
    )

    status = models.CharField(verbose_name="Status", max_length=1, choices=ORDER_STATUS, blank=True, default='p')

    def is_overdue(self):
        return self.due_back and timezone.now().date() > self.due_back

    def __str__(self):
        return f'{self.car} ({self.date})'

    def total(self):
        result = 0
        for line in self.lines.all():
            result += line.service_price() * line.quantity
        return result


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order",
                              on_delete=models.CASCADE,
                              related_name='lines',)
    service = models.ForeignKey(to="Service",
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)
    quantity = models.IntegerField(default=1)

    def line_sum(self):
        return self.service.price * self.quantity

    def service_price(self):
        return self.service.price

    def __str__(self):
        return f' {self.service} - {self.quantity}'
