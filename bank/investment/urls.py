from django.urls import path
from . import views

urlpatterns = [
    path('/create' ,  views.create_user ,  name='create_user'  ) , 
    path('/', views.welcome, name='welcome'),
    path('/about' ,  views.aboutUs ,  name  = 'about'),
    path('/predictions' ,  views.see_predictions ,   name=  'predictions') , 
    path('/investors' ,  views.see_investors ,  name= 'see_investors'),
   
   
]   