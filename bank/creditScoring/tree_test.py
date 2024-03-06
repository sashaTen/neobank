import pickle
import    pandas  as  pd



data = {
    'credit.policy': [1.0],
    'int.rate': [0.14],
    'installment': [548.90],
    'dti': [14.67],
    'fico': [682.000]
}

new_data = pd.DataFrame(data)
# Load the decision tree model
with open("tree_model_credit_score.sav", "rb") as model_file:
    loaded_decision_tree = pickle.load(model_file)
predictions = loaded_decision_tree.predict(new_data)

print(predictions)

#  python  tree_test.py