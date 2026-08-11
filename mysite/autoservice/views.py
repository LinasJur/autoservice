from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Car, Order, OrderLine
# Create your views here.

def index(request):
    context = {
        'num_services' : Service.objects.count(),
        'num_cars' : Car.objects.count(),
        'num_done_orders' : Order.objects.filter(status= 'į').count(),
    }
    return render(request, template_name='index.html', context=context)