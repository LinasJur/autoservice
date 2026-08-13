from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Service, Car, Order, OrderLine
# Create your views here.

def index(request):
    context = {
        'num_services' : Service.objects.count(),
        'num_cars' : Car.objects.count(),
        'num_done_orders' : Order.objects.filter(status= 'į').count(),
    }
    return render(request, template_name='index.html', context=context)


def cars(request):
    context = {
        'cars' : Car.objects.all(),
    }
    return render(request, template_name='cars.html', context=context)

def car(request, car_pk):
    context = {
        'car' : Car.objects.get(pk=car_pk),
    }
    return render(request, template_name='car.html', context=context)

class OrdersListView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'
    paginate_by = 3

class OrdersDetailView(generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'