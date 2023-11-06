from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_base, name='inventory_base'),
    path('supply/', views.supply_page, name='supply_page'),
    path('orders/',views.orders_page, name='orders_page'),
    path('register-vendor/', views.register_vendor, name='register_vendor'),
    path('order-log/', views.order_logs_page, name='order_log'),
    path('order-log/log-order',views.log_order, name='log_order'),
    path('order-log/history/', views.order_history, name='order_history'),
    path('vendors/', views.vendors_page, name='vendors_page'),
    path('items/',views.items_page, name='items_page'),
    path('register-item/',views.register_item, name='register_item'),
    path('order-log/save-log/',views.save_logs,name='save_logs'),
    path('orders/pending-orders/',views.pending_orders,name='pending_orders'),
    path('orders/completed-orders',views.completed_orders,name='completed_orders'),

    # Define other URL patterns for the inventory app here
]
