from django.urls import path
from . import views

urlpatterns = [
    path('/create' ,  views.create_user ,  name='create_user'  ) , 
    path('/<int:company_id>/', views.welcome, name='welcome'),
    path('/about' ,  views.aboutUs ,  name  = 'about'),
    path('/investors' ,  views.see_investors ,  name= 'see_investors'),
   
   
]   