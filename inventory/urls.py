from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_base, name='inventory_base'),
    path('supply/', views.supply_page, name='supply_page'),
    path('register-vendor/', views.register_vendor, name='register_vendor'),
    path('order-log/', views.order_logs_page, name='order_log'),
    path('order-logs/history/', views.order_history, name='order_history'),
    path('vendors/', views.vendors_page, name='vendors_page'),

    # Define other URL patterns for the inventory app here
]
