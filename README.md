# 🧠 Fake News Detection System

A Machine Learning-based web application that classifies news articles as **REAL** or **FAKE** using Natural Language Processing (NLP) and supervised learning models.

---

## 🚀 Overview

This project uses text classification techniques to detect misinformation in news articles. It processes raw text, extracts features using TF-IDF, and applies a trained ML model to make predictions in real-time through a Flask web application.

---

## 🎯 Features

- 🧠 Fake vs Real news classification
- ⚡ Fast real-time predictions
- 🧹 Advanced text preprocessing (cleaning, stemming, stopwords removal)
- 📊 TF-IDF feature extraction
- 🌐 Simple and interactive Flask web interface
- 🔁 Reusable ML pipeline (train → save → predict)

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **Scikit-learn**
- **NLTK**
- **Pandas**
- **NumPy**
- **HTML / CSS**

---

## 📂 Project Structure

---

```
fake-news-detector/
│
├── app.py # Flask web application
├── train_model.py # Model training script
├── predict.py # CLI prediction script
│
├── Fake.csv # Fake news dataset
├── True.csv # Real news dataset
│
├── fake_news_model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
│
├── templates/
│ └── index.html # Frontend UI
│
├── static/
│ └── style.css # Styling
│
└── README.md
```

---


---

## ⚙️ How It Works

### 1. Data Preprocessing
- Convert text to lowercase
- Remove special characters & punctuation
- Remove stopwords
- Apply stemming using Porter Stemmer

### 2. Feature Extraction
- Convert text into numerical features using **TF-IDF Vectorizer**

### 3. Model Training
- Train a classification model (Logistic Regression / Naive Bayes)
- Evaluate performance using accuracy & classification report

### 4. Prediction
- User enters news text
- System predicts:
  - ✅ REAL NEWS
  - ❌ FAKE NEWS

---

## ▶️ Installation & Setup

### 1. Clone repository
```bash
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
 Install dependencies
 pip install -r requirements.txt 