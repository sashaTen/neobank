from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse
from .forms   import  InvestorForm
from .models import Investor
from .get_data import forecast
# Create your views here.
def welcome(request ):
  return render(request, 'welcome.html')


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


def see_investors(request):
     objects = Investor.objects.all()
     res ='Printing all Dreamreal entries in the DB : <br>'
   
     for elt in objects:
       res += elt.name+"<br>"
    
     return HttpResponse(res)




def see_predictions(request):
    '''
    predictions = forecast("AAPL", "2020-01-01", "2021-01-01", 40, 3)
    
    # Convert NumPy array to a list
    predictions_list = predictions.tolist()
    
    # Return as JSON response
    return JsonResponse({'predictions': predictions_list})
    
    '''
 
    return HttpResponse('predictions ')