from django.urls import path
from . import views

urlpatterns = [
    # path('bday/',views.schedule_birthday_check, name='bday'),
    path('register-user/', views.register_user, name='register_user'),
 
    path('logout/', views.logout_user, name='logout_user'),
    path('students/',views.students_page, name='students_page'),
    path('franchise/', views.franchise_page, name='franchise_page'),
    path('franchise/delete/<int:user_id>/',views.delete_franchisee, name='delete_franchisee'),
    path('franchise/edit/<int:user_id>/', views.edit_login, name='edit_login'),
    path('', views.academy_base, name='academy_base'),
    path('franchise-details/<int:user_id>/',views.franchise_details, name='franchise_details'),
    path('teacher/', views.teachers_page, name='teachers_page'),
    path('teacher-details/<int:user_id>/',views.teacher_details, name='teacher_details'),
    path('teacher/delete/<int:user_id>/',views.delete_teacher, name='delete_teacher'),
    path('teacher/edit/<int:user_id>/', views.edit_login, name='edit_login'),
    path('teacher-level-form/<int:user_id>/', views.teacher_level_form, name='teacher_level_form'),




]