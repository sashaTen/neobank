import os
import pickle
import pandas as pd

# Define the path to the model file
dir_path = os.path.dirname(os.path.realpath(__file__))
model_file_path = os.path.join(dir_path, "tree_model_credit_score.sav")

def predict(policy, rate, installment, dti, fico):
    """
    Predict credit score using a decision tree model.

    Parameters:
    - policy: Credit policy (float)
    - rate: Interest rate (float)
    - installment: Installment amount (float)
    - dti: Debt-to-income ratio (float)
    - fico: FICO score (float)

    Returns:
    - predictions: Predicted credit scores (array-like)
    """
    # Validate input parameters if necessary

    # Create DataFrame with input data
    data = {
        'credit.policy': [policy],
        'int.rate': [rate],
        'installment': [installment],
        'dti': [dti],
        'fico': [fico]
    }
    new_data = pd.DataFrame(data)

    try:
        # Load the decision tree model
        with open(model_file_path, "rb") as model_file:
            loaded_decision_tree = pickle.load(model_file)
        
        # Make predictions
        predictions = loaded_decision_tree.predict(new_data)
        return predictions
    except Exception as e:
        print("Error occurred during prediction:", e)
        return None



'''
build ml model into app -> 
      ->mlops and ml system-
           ->api book and clean code
               -> add new features  
                   -> new features 
                         -> inspiration from other fintechs
                             -> be your  specialization 
                                   the ai for insurance and lending and  banking
                                 -> learn economics/finance/bank-management principles
-> / how other's found differentiation by reading and then think about 
    /problems thinking about proccess  
    /ai-data value research/
-> read be your  specialization the ai for insurance and lending and  banking
always think how to  make proccess of  insurance and lending and  banking better?
                     -faster/cheapier/productive/ ai values to it.  
-> read  ai    research  top  papers  and  news and  articles a lot. 
you need 3 levels: 
your rivals 
your indusry 
major general best. 
* always seek feedbacks and networking is key. 
* постоянное саморазвитие, 
'''