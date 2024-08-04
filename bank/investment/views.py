from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms   import  InvestorForm
# Create your views here.
def welcome(request , company_id):
    top_stocks = ['apple' ,  'microsoft' ,  'google']
     
    return render(request, 'welcome.html', {'company_name': top_stocks[company_id] })


def create_user(request): 
      if request.method == 'POST':
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')  # Redirect to a success page or investor list
      else:
        form = InvestorForm()
    
      return render(request, 'create_user.html', {'form': form})
 



def aboutUs(request):
    return  render(request  ,  'about.html')


