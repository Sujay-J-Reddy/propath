from django.urls import path
from . import views

urlpatterns = [
    path('register-user/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('students/',views.students_page, name='students_page'),
    path('franchise/', views.franchise_page, name='franchise_page'),
    path('franchise/delete/<int:user_id>/',views.delete_franchisee, name='delete_franchisee'),
    path('franchise/edit/<int:user_id>/', views.edit_login, name='edit_login'),
    path('', views.academy_base, name='academy_base'),
    path('franchise-details/<int:user_id>/',views.franchise_details, name='franchise_details'),
    path('teacher/', views.teachers_page, name='teachers_page'),
    path('teacher/feedbacks/', views.teacher_feedbacks, name='teacher_feedbacks'),
    path('teacher-details/<int:user_id>/',views.teacher_details, name='teacher_details'),
    path('teacher/delete/<int:user_id>/',views.delete_teacher, name='delete_teacher'),
    path('teacher/edit/<int:user_id>/', views.edit_login, name='edit_login'),
    path('teacher-level-form/<int:user_id>/', views.teacher_level_form, name='teacher_level_form'),
    path('certificates/', views.certificate_requests, name='certificate_requests'),
    path('competitions/', views.competitions_page, name='competitions_page'),
    path('competitions/entries/', views.competition_entries, name='competition_entries'),
    path('competitins/winners', views.competition_winners, name='competition_winners'),
    path('birthdays/', views.check_birthdays, name='check_birthdays'),
    path('schools/', views.schools_page, name='schools_page'),
    path('schools/regsiter/', views.register_school, name='register_school'),
    path('schools/order/', views.school_order, name='school_order'),
]