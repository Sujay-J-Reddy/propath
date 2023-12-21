from django.urls import path
from . import views
from .views import LoginView
from academy.views import enquiry

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', views.landing_page, name='landing_page'),
    path('enquiry/',enquiry, name='enquiry'),

]
