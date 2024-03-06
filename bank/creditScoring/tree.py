import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import pickle






path   =  'https://raw.githubusercontent.com/Usangajonah/Loan-Prediction-/main/loan_data.csv'
loans = pd.read_csv(path)
print(loans.info())
cat_feats = ['purpose']
final_data = pd.get_dummies(loans,columns=cat_feats,drop_first=True)
final_data.info()
selected_features = ['credit.policy', 'int.rate', 'installment',  'dti', 'fico']
X = final_data.loc[:, selected_features]
y = final_data['not.fully.paid']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)
predictions = dtree.predict(X_test)
print(classification_report(y_test,predictions))


pickle.dump(dtree,open("tree_model_credit_score.sav", "wb"))

print(X_train.iloc[0])
