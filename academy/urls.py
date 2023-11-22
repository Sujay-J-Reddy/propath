from django.urls import path
from . import views

urlpatterns = [
    # path('bday/',views.schedule_birthday_check, name='bday'),
    path('register-user/', views.register_user, name='register_user'),
    path('register-user/franchisee', views.register_franchisee, name='register_franchisee'),
    path('register-user/admin/', views.register_admin, name='register_admin'),
    path('logout/', views.logout_user, name='logout_user'),
    path('students/',views.students_page, name='students_page'),
    path('franchise/', views.franchise_page, name='franchise_page'),
    path('franchise/delete/<int:franchisee_id>/',views.delete_franchisee, name='delete_franchisee'),
    path('franchise/edit/<int:franchisee_id>/', views.edit_franchisee, name='edit_franchisee'),
    path('', views.academy_base, name='academy_base'),
    # path('franchise/',views.franchise_page, name='franchise_page'),
]