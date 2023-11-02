from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_base, name='inventory_base'),
    path('supply/', views.supply_page, name='supply_page'),
    path('register-vendor/', views.register_vendor, name='register_vendor'),
    path('order-log/', views.order_logs_page, name='order_log'),
    path('order-log/log-order',views.log_order, name='log_order'),
    path('order-log/history/', views.order_history, name='order_history'),
    path('vendors/', views.vendors_page, name='vendors_page'),
    path('order-log/save-log/',views.save_logs,name='save_logs'),

    # Define other URL patterns for the inventory app here
]
