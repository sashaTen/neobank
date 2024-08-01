from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request , company_id):
    top_stocks = ['apple' ,  'microsoft' ,  'google']
     
    return render(request, 'welcome.html', {'company_name': top_stocks[company_id] })


   



def aboutUs(request):
    return  render(request  ,  'about.html')


