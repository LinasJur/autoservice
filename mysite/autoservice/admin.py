from django.contrib import admin
from .models import Service , Car, Order, Order_line
# Register your models here.

admin.site.register(Service)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Order_line)