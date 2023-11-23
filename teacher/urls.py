from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_base, name='teacher_base'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('profile/',views.teacher_profile, name='teacher_profile')
]