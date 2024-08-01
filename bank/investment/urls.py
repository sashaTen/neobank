from django.urls import path
from . import views

urlpatterns = [
    path('/<int:company_id>/', views.welcome, name='welcome'),
    path('/about' ,  views.aboutUs ,  name  = 'about'),
   
   
]   