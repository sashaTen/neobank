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
  policy = request.POST['policy']
  rate   = request.POST['rate']
  installment   =    request.POST['installment']
  dti  =    request.POST['dti']
  fico  =   request.POST['fico']
  result   =    predict(policy ,  dti , installment ,   fico ,   rate)
  context   =  {
        'result'  :    result}
     
      
     
     
  return render(request ,    'result.html'  , context ) # context  )
      # python manage.py runserver 



#  https://www.youtube.com/watch?v=M_yKXx7xEW4     
#   the  submit  btn    calls   result   url  which  
# then    calls the   result   function  in   views  
#  which    get the  data  and  then   gets   POST  data  
#  then    uses     ml    model  which  is  saved  in    tree_model 
#   then   gives  the  prediction  