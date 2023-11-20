from django.urls import path, re_path
from . import views


urlpatterns = [
    path('',views.base_page, name='base_page'),
    path('orders/',views.orders, name='orders'),
    path('orders/new-order', views.new_order, name='new_order'),
    path('orders/orders-completed',views.orders_completed, name='orders_completed'),
    path('orders/orders-pending', views.orders_pending, name='orders_pending'),
    path('students/', views.students, name='students'),
    path('students/register-student/', views.register_student, name='register_student'),
    re_path(r'^students/edit/(?P<student_id>[\w-]+)/$', views.edit_student, name='edit_student'),
    re_path(r'^students/delete/(?P<student_id>[\w-]+)/$', views.delete_student, name='delete_student'),
]

    # Define other URL patterns for the inventory app here

