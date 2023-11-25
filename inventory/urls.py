from django.urls import path
from . import views


urlpatterns = [
    path('', views.inventory_base, name='inventory_base'),
    path('supply/', views.supply_page, name='supply_page'),
    path('orders/',views.orders_page, name='orders_page'),
    path('register-vendor/', views.register_vendor, name='register_vendor'),
    path('register-kit/', views.register_kit, name='register_kit'),
    path('order-log/', views.order_logs_page, name='order_log'),
    path('order-log/log-order',views.log_order, name='log_order'),
    path('order-log/history/', views.order_history, name='order_history'),
    path('vendors/', views.vendors_page, name='vendors_page'),
    path('kits/', views.kits_page, name='kits_page'),
    path('kit/delete/<int:kit_id>/',views.delete_kit, name='delete_kit'),
    path('kit/edit/<int:kit_id>/', views.edit_kit, name='edit_kit'),
    path('vendor/delete/<int:vendor_id>/',views.delete_vendor, name='delete_vendor'),
    path('vendor/edit/<int:vendor_id>/', views.edit_vendor, name='edit_vendor'),
    path('items/',views.items_page, name='items_page'),
    path('items/delete/<int:item_id>/',views.delete_item, name='delete_item'),
    path('items/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('register-item/',views.register_item, name='register_item'),
    path('order-log/save-log/',views.save_logs,name='save_logs'),
    path('orders/update-orders/', views.update_orders, name='update_orders'),
    path('orders/pending-orders/',views.pending_orders,name='pending_orders'),
    path('orders/completed-orders',views.completed_orders,name='completed_orders'),
    path('orders/log-pending/',views.log_pending, name='log_pending'),


    # Define other URL patterns for the inventory app here
]
