from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .tree_test import predict
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.http import JsonResponse
from  .mlflow_tutorial import sentiment_analysis,prepare_data_for_inference


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



def train_model(request):
    # Load data
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

    # Start an MLflow experiment
    with mlflow.start_run():
        # Train a model
        clf = RandomForestClassifier(n_estimators=100)
        clf.fit(X_train, y_train)

        # Predict
        predictions = clf.predict(X_test)
        acc = accuracy_score(y_test, predictions)

        # Log model and metrics to MLflow
        mlflow.sklearn.log_model(clf, "model")
        mlflow.log_metric("accuracy", acc)

        # Return a JSON response with the accuracy
        return JsonResponse({"accuracy": acc})






def  sentiment(request):
    df = pd.read_csv('https://raw.githubusercontent.com/surge-ai/stock-sentiment/main/sentiment.csv')
    
    sentiment = request.POST['sentiment']
    
    
      # Extract X and y
    X = df['Tweet Text']
    y = df['Sentiment']
    rf_classifier, tfidf_vectorizer = sentiment_analysis(X, y)
# Now, prepare new text data for inference
    new_texts = [sentiment]
    # Predict the sentiment of the new texts
    predictions = prepare_data_for_inference(new_texts, rf_classifier, tfidf_vectorizer)
    return HttpResponse( predictions )

    


