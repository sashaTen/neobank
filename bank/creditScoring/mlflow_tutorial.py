import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import nltk

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

def preprocess_and_vectorize(X):
    # Helper function to preprocess individual texts
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

    # Apply preprocessing to the entire dataset
    X_preprocessed = [preprocess_text(text) for text in X]

    # Vectorize the preprocessed text using TF-IDF
    tfidf_vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')
    X_tfidf = tfidf_vectorizer.fit_transform(X_preprocessed)

    return X_tfidf

# Apply the function to preprocess and vectorize the text data





def sentiment_analysis(X , y):
    X_processed = preprocess_and_vectorize(X)

# Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

    # Train a Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Predict the sentiment of the test set
    y_pred = rf_classifier.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy  





