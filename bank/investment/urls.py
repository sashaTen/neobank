from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('/about' ,  views.aboutUs ,  name  = 'about'),
   
   
]   