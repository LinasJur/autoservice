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
                            blank=True,
                            related_name='orders')
    date = models.DateTimeField(auto_now_add=True)

    ORDER_STATUS = (
        ('p' , 'Patvirtinta'),
        ('v' , 'Vykdoma'),
        ('a' , 'Atšaukta'),
        ('į' , 'Įvykdyta'),
    )

    status = models.CharField(verbose_name="Status", max_length=1, choices=ORDER_STATUS, blank=True, default='p')

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
