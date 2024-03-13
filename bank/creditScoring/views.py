from django.shortcuts import render
from django.http import HttpResponse
from .tree_test import predict





def hello(request):
      result   =    predict(1.0 ,    1.58 ,    548.00 ,   84.00 ,    600.00)
      context   =  {
        'result'  :    result}
      return render(request ,    'home.html'   ,  context   )


