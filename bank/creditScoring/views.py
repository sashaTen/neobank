from django.shortcuts import render
from django.http import HttpResponse
from .tree_test import predict





def hello(request):
      result   =    predict(0.1 ,    1.58 ,    548.00 ,   84.00 ,    600.00)
      context   =  {
        'result'  :    result}
      return render(request ,    'home.html'   ,  context   )

'''
 - policy: Credit policy (float)
    - rate: Interest rate (float)
    - installment: Installment amount (float)
    - dti: Debt-to-income ratio (float)
    - fico: FICO score (float)
'''



def  result(request):
      result   =    predict(0.1 ,    1.58 ,    548.00 ,   84.00 ,    600.00)
      context   =  {
        'result'  :    result}
     
      return render(request ,    'result.html'  ,  context  )
      