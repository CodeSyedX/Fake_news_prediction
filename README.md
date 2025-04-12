# 🔤 Fake News Detector

A full-stack machine learning web app that predicts whether a news article is **Real** or **Fake**, enhanced with **Google Fact Check** API for additional credibility verification.

![Fake News Detector Banner](https://img.shields.io/badge/ML-Logistic%20Regression-blue) ![Backend-Flask](https://img.shields.io/badge/Backend-Flask-lightgrey) ![Frontend-HTML/CSS/JS](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange)

---

## 🚀 Features

- ✅ Predicts if the news is *real* or *fake* using a trained ML model
- 🔍 Uses **TF-IDF** and **Logistic Regression**
- 🧪 Real-time **Google Fact Check API** integration
- 💻 Clean front-end for user interaction
- 📦 Flask REST API backend

---

## 📁 Project Structure

```
📆 fake-news-detector/
├── train_model.py              # ML model training
├── fake_news_model.pkl        # Saved model
├── tfidf_vectorizer.pkl       # Saved TF-IDF vectorizer
├── app.py                     # Flask backend
├── index.html                 # Front-end UI
├── requirements.txt           # Python dependencies
└── .env                       # API key for Google Fact Check
```

---

## 🧠 Model Details

- **Algorithm:** Logistic Regression
- **Text Processing:**
  - Lowercasing
  - Removing non-alphabet characters
  - Removing stopwords
  - Stemming (Porter)
- **Feature Extraction:** TF-IDF
- **Training Accuracy:** ~97%  
- **Testing Accuracy:** ~94%

---

## 🔐 Google Fact Check API

To enhance predictions, the app queries Google's Fact Check Tools and shows related claims.

**Steps:**

1. Get your API Key from [Google Fact Check API](https://developers.google.com/fact-check/tools/api)
2. Create a `.env` file:
   ```
   GOOGLE_FACTCHECK_API_KEY=your_api_key_here
   ```

---

## 💻 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model (if not already trained)

```bash
python train_model.py
```

### 4. Run the Flask app

```bash
python app.py
```

### 5. Open the front-end

Just open `index.html` in your browser (served from root route `/`).

---

## 🔀 API Endpoint

**POST** `/predict`  
Content-Type: `application/json`

**Request body:**
```json
{
  "text": "The article you want to check."
}
```

**Response:**
```json
{
  "prediction": "Fake News",
  "fact_check": [
    {
      "claim": "...",
      "rating": "...",
      "publisher": "...",
      "url": "..."
    }
  ]
}
```

---

## 🌐 Deployment (Optional)

You can deploy the Flask backend using:

- [Render](https://render.com/)
- [Railway](https://railway.app/)
- Docker (with gunicorn/nginx)

---



## 🧑‍💻 Author

**CodeSyedX**  
💼 GitHub: [github.com/CodeSyedX](https://github.com/CodeSyedX)

---

