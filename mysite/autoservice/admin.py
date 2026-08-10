from django.contrib import admin
from .models import Service , Car, Order, Order_line
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'date']

class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'license_plate' , 'vin_code', 'client_name']
    list_filter = ['client_name', 'make', 'model']
    search_fields = ['license_plate', 'vin_code']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['order', 'service', 'quantity']



admin.site.register(Service, ServiceAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_line, OrderLineAdmin)