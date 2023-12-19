from django.urls import path
from . import views
from .views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', views.landing_page, name='landing_page'),
    path('about_us/', views.about_us, name='about_us'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
