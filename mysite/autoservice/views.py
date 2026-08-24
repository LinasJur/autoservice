from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic.edit import FormMixin
from .forms import OrderCommentForm, UserChangeForm, ProfileChangeForm
from .models import Service, Car, Order, OrderLine





# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_services' : Service.objects.count(),
        'num_cars' : Car.objects.count(),
        'num_done_orders' : Order.objects.filter(status= 'į').count(),
        'num_visits' : num_visits,
    }
    return render(request, template_name='index.html', context=context)


def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {
        'cars' : paged_cars,
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

class OrdersDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'
    form_class = OrderCommentForm

    def get_success_url(self):
        return reverse('order', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.order = self.get_object()
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

def search(request):
    query = request.GET.get('query')
    context = {
        'query' : query,
        'cars' : Car.objects.filter(Q(make__icontains=query) |
                                    Q(model__icontains=query) |
                                    Q(license_plate__icontains=query) |
                                    Q(vin_code__icontains=query) |
                                    Q(client_name__icontains=query)),
    }
    return render(request, template_name='search.html', context=context)

class UserOrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'user_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(car_owner=self.request.user)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

@login_required
def profile(request):
    u_form = UserChangeForm(request.POST or None, instance=request.user)
    p_form = ProfileChangeForm(request.POST or None, request.FILES, instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        return redirect("profile")

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, template_name="profile.html", context=context)

