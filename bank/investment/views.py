from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse('welcome page . start investing  and  bring   your   portfolio')



def aboutUs(request):
    return  HttpResponse('our team gives  the  best  analysis  of your portfolio using the state of art techniques')


def plansDaylyAnalysis(request):
    return  HttpResponse('today i did   :  1   python startapp invest   2 regsiter in main setting the app 3   include urls of app in main  4 urls with propoer / 5 wrote basic views .    my plan  for  future  ')