from django.urls import path
from . import views
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', views.landing_page, name='landing_page'),


]
