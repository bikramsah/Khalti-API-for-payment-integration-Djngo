from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.home,name="home"),
    path('initiate',views.initkhalti,name="initiate"),
    path('verify',views.verifyKhalti,name="verify")
]