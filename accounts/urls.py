from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('franchisee_dashboard/', views.franchisee_dashboard_view, name='franchisee_dashboard'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),

]
