
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.http import JsonResponse

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
