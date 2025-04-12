from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_FACTCHECK_API_KEY")

# Download stopwords if not already
nltk.download('stopwords')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load ML model and vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
stemmer = PorterStemmer()

def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text).lower().split()
    text = [stemmer.stem(word) for word in text if word not in stopwords.words('english')]
    return ' '.join(text)

def check_fact(fact_check_result):
    if not fact_check_result:
        return "⚠️ No matching fact-checks found."
    else:
        return fact_check_result

def check_fact_google_fact_check(news_text, api_key):
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        'query': news_text,
        'key': api_key,
        'languageCode': 'en'
    }
    
    response = requests.get(url, params=params)
    result = response.json()
    
    fact_checks = []
    if 'claims' in result:
        for claim in result['claims']:
            fact_checks.append({
                "claim": claim.get('text'),
                "rating": claim['claimReview'][0].get('textualRating'),
                "publisher": claim['claimReview'][0]['publisher'].get('name'),
                "url": claim['claimReview'][0].get('url')
            })
    return fact_checks

@app.route('/')
def index():
    return send_from_directory('', 'index.html')  # Serves index.html in root

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_text = data.get('text')
    
    if not input_text:
        return jsonify({'error': 'No text provided'}), 400

    # Preprocess and predict
    processed_text = preprocess(input_text)
    vectorized = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized)[0]
    result = 'Fake News' if prediction == 1 else 'Real News'

    # Also get real-time fact checks
    fact_checks = check_fact_google_fact_check(input_text, api_key)
    fact_check_result = check_fact(fact_checks)

    return jsonify({
        'prediction': result,
        'fact_check': fact_check_result
    })

if __name__ == '__main__':
    app.run(debug=True)
