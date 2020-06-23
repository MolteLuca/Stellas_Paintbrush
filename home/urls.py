from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry, name='portfolio-entry'),
    path('home/', views.home, name='portfolio-home'),
    path('home/confirm', views.home, name='portfolio-confirm')
]