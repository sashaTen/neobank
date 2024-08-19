import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import mlflow
import nltk
from sklearn.linear_model import LogisticRegression
# Download the 'punkt' tokenizer model
nltk.download('punkt_tab')
nltk.download('punkt')        # Tokenizer models
nltk.download('stopwords')    # List of common stopwords
nltk.download('wordnet')      # WordNet lemmatizer
nltk.download('omw-1.4')      # WordNet data (optional, for improved lemmatization)

# Load the data
df = pd.read_csv('https://raw.githubusercontent.com/surge-ai/stock-sentiment/main/sentiment.csv')

# Extract X and y
X = df['Tweet Text']
y = df['Sentiment']

# Function to preprocess and vectorize the text data
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


# Function to preprocess the text
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Remove numbers
    tokens = [word for word in tokens if not word.isdigit()]

    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join tokens back into a single string
    processed_text = ' '.join(tokens)
    return processed_text

# Function to vectorize the text using a pre-fitted TF-IDF vectorizer
def vectorize_text(texts, tfidf_vectorizer):
    # Preprocess the text
    texts_preprocessed = [preprocess_text(text) for text in texts]
    
    # Vectorize the preprocessed text using the pre-fitted vectorizer
    X_tfidf = tfidf_vectorizer.transform(texts_preprocessed)
    
    return X_tfidf
def sentiment_analysis(X, y):
    mlflow.set_experiment('Baseline Model')
    with mlflow.start_run():
        X_preprocessed = [preprocess_text(text) for text in X]
        tfidf_vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')
        X_tfidf = tfidf_vectorizer.fit_transform(X_preprocessed)
        X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)
        rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_classifier.fit(X_train, y_train)
        y_pred = rf_classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        mlflow.log_metric('accuracy', accuracy)
        
        mlflow.sklearn.log_model(rf_classifier, 'random forest model')

        mlflow.set_tag('developer', 'Alex')
        mlflow.set_tag('preprocessing', 'None')
        mlflow.set_tag('model', 'random forest model')
    
    return rf_classifier, tfidf_vectorizer
def prepare_data_for_inference(new_texts, classifier, tfidf_vectorizer):
    # Preprocess and vectorize the new text data using the trained vectorizer
    X_new_tfidf = vectorize_text(new_texts, tfidf_vectorizer)
    
    # Predict the sentiment of the new data
    predictions = classifier.predict(X_new_tfidf)
    
    return predictions
# Assuming you have your training data X and y



def sentiment_analysis_logistic(X, y):
    mlflow.set_experiment('Baseline Model')
    with mlflow.start_run():
    # Preprocess and vectorize the text data
        X_preprocessed = [preprocess_text(text) for text in X]

        # Initialize and fit the TF-IDF vectorizer
        tfidf_vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')
        X_tfidf = tfidf_vectorizer.fit_transform(X_preprocessed)

        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

        # Train a Random Forest classifier
        logistic_classifier =LogisticRegression()
        logistic_classifier.fit(X_train, y_train)
    

        # Predict the sentiment of the test set
        y_pred =  logistic_classifier .predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        mlflow.log_metric('accuracy', accuracy)
        
        mlflow.sklearn.log_model(logistic_classifier, 'logistic_classifier')

        mlflow.set_tag('developer', 'Alex')
        mlflow.set_tag('preprocessing', 'None')
        mlflow.set_tag('model', 'logistic_classifier')

    # Return the trained model and vectorizer for future use
    return  logistic_classifier , tfidf_vectorizer