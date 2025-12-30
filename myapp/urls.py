from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('initiate/', views.initkhalti, name='initiate'),
    path('verify/', views.verifyKhalti, name='verify'),
]
