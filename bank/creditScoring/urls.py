from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('iris_mlflow/'  ,  views.train_model , name =   'iris_mlflow'), 
    path('sentiment/' ,   views.sentiment ,  name = 'sentiment'),
    path('result/' ,   views.result  ,  name= 'result')
]   