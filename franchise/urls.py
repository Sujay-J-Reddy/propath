from django.urls import path
from . import views


urlpatterns = [
    path('',views.base_page, name='base_page'),
    path('orders/',views.orders, name='orders'),
    path('orders/new-order', views.new_order, name='new_order'),
    path('orders/orders-completed',views.orders_completed, name='orders_completed'),
    path('orders/orders-pending', views.orders_pending, name='orders_pending'),

    # Define other URL patterns for the inventory app here
]
