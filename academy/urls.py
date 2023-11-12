from django.urls import path
from . import views

urlpatterns = [
    path('register-user/', views.register_user, name='register_user'),
    path('register-user/franchisee', views.register_franchisee, name='register_franchisee'),
    path('register-user/admin/', views.register_admin, name='register_admin'),
    path('logout/', views.logout_user, name='logout_user'),
    path('', views.academy_base, name='academy_base'),
    # path('franchise/',views.franchise_page, name='franchise_page'),
]