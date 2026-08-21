
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_pk>/', views.car, name='car'),
    path('orders/', views.OrdersListView.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrdersDetailView.as_view(), name='order'),
    path('search/', views.search, name = 'search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('myorders/' , views.UserOrderListView.as_view(), name='my_orders'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
