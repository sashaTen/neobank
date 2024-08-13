from django.shortcuts import render , redirect
import matplotlib.pyplot as plt
import io
import urllib, base64
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
     predictions  , y_test= forecast("AAPL", "2020-01-01", "2021-01-01", 40, 3)
    
    
    
    
    plt.figure(figsize=(7, 5))  # Adjust figure size as needed
    plt.plot( y_test, label='Actual Data')
    plt.plot(predictions, label='LSTM Predicted Data ')

    plt.xlabel('Time Step')
    plt.ylabel('Price')
    plt.title('Actual vs. Predicted Stock Prices   ' )
    plt.legend()
    plt.grid(True)

    # Show the plot
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Encode the image in base64
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    
    
 
    return render(request, 'about.html', {'plot_data': uri})
    '''
    
    return HttpResponse('predictions page ')