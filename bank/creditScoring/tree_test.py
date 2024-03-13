import pickle
import    pandas  as  pd
import   os 


'''

data = {
    'credit.policy': [1.0],
    'int.rate': [0.84],
    'installment': [548.90],
    'dti': [74.67],
    'fico': [682.000]
}

new_data = pd.DataFrame(data)
# Load the decision tree model
with open("tree_model_credit_score.sav", "rb") as model_file:
    loaded_decision_tree = pickle.load(model_file)
predictions = loaded_decision_tree.predict(new_data)

print(predictions)
'''
#  python  tree_test.py
dir_path = os.path.dirname(os.path.realpath(__file__))
model_file_path = os.path.join(dir_path, r"tree_model_credit_score.sav")


def    predict(policy ,   rate,      installment ,    dti   ,    fico):
    data = {
    'credit.policy': [policy],
    'int.rate': [rate],
    'installment': [installment],
    'dti': [dti],
    'fico': [fico]
}
    new_data = pd.DataFrame(data)
# Load the decision tree model
    with open(model_file_path, "rb") as model_file:
        loaded_decision_tree = pickle.load(model_file)
    predictions = loaded_decision_tree.predict(new_data)
    return   predictions

