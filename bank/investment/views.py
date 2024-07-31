from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse('welcome page . start investing  and  bring   your   portfolio')



def aboutUs(request):
    return  HttpResponse('our team gives  the  best  analysis  of your portfolio using the state of art techniques')