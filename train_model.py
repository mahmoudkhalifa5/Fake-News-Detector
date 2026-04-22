# train_model.py

import pandas as pd
import re
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nltk.download('stopwords')

# ==================== Load Dataset ====================

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# إضافة label
fake["label"] = 1   # FAKE
true["label"] = 0   # REAL

# دمج
df = pd.concat([fake, true])

# استخدم النص فقط
df = df[["text", "label"]]

print(df.head())
print(df['label'].value_counts())

# ==================== Cleaning ====================
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]
    return ' '.join(words)

df['cleaned'] = df['text'].apply(clean_text)

# ==================== Vectorization ====================
vectorizer = TfidfVectorizer(max_features=10000)
X = vectorizer.fit_transform(df['cleaned'])
y = df['label']

# ==================== Train ====================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

# ==================== Evaluate ====================
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# ==================== Save ====================
pickle.dump(model, open("fake_news_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model saved!")