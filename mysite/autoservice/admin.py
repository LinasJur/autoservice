from django.contrib import admin
from .models import Service , Car, Order, OrderLine
# Register your models here.

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0
    readonly_fields = ['line_sum', 'service_price']
    fields = ['service', 'quantity', 'service_price', 'line_sum']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'date', 'total', 'status']
    inlines = [OrderLineInLine]
    list_editable  = ['status']
    readonly_fields = ['date', 'total']
    fieldsets = [
        ('General', {'fields': ('car', 'date', 'total')}),
        ('Status', {'fields': ('status',)}),
    ]

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
admin.site.register(OrderLine, OrderLineAdmin)