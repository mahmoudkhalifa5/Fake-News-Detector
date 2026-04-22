# # fake_news_detector.py
# # Fake News Detection Project

# import pandas as pd
# import re
# import pickle
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, classification_report

# # Download stopwords (only once)
# nltk.download('stopwords')

# # ==================== 1. Data Preparation ====================
# df = pd.read_csv("data.csv")

# # ==================== 2. Text Cleaning ====================
# stop_words = set(stopwords.words('english'))
# stemmer = PorterStemmer()

# def clean_text(text):
#     text = text.lower()
#     text = re.sub(r'[^a-zA-Z\s]', '', text)
#     words = text.split()
#     words = [stemmer.stem(word) for word in words if word not in stop_words]
#     return ' '.join(words)

# df['cleaned_text'] = df['text'].apply(clean_text)

# # ==================== 3. Feature Extraction ====================
# vectorizer = TfidfVectorizer(max_features=5000)
# X = vectorizer.fit_transform(df['cleaned_text'])
# y = df['label']

# # ==================== 4. Train Model ====================
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# model = LogisticRegression()
# model.fit(X_train, y_train)

# # ==================== 5. Evaluation ====================
# y_pred = model.predict(X_test)

# print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
# print("\nClassification Report:")
# print(classification_report(y_test, y_pred, target_names=['REAL', 'FAKE']))

# # ==================== 6. Save Model ====================
# with open('fake_news_model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# with open('vectorizer.pkl', 'wb') as f:
#     pickle.dump(vectorizer, f)

# print("\nModel and vectorizer saved successfully!")

# # ==================== 7. Prediction Function ====================
# def predict_news(news_text):
#     cleaned = clean_text(news_text)
#     vec = vectorizer.transform([cleaned])
#     pred = model.predict(vec)[0]
#     return "FAKE ❌" if pred == 1 else "REAL ✅"

# # ==================== 8. Test ====================
# print("\nTesting on new samples:")
# print("-" * 50)

# test_news = [
#     "NASA confirms landing on Mars",
#     "Earth is flat says new study",
#     "Scientists discover new galaxy",
#     "Vaccine contains tracking devices"
# ]

# for news in test_news:
#     result = predict_news(news)
#     print(f"News: {news}")
#     print(f"Prediction: {result}\n")

# # ==================== 9. Interactive Mode ====================
# print("\nFake News Detector is ready!")
# print("Type 'exit' to quit")

# while True:
#     user_input = input("\nEnter news: ")
#     if user_input.lower() == 'exit':
#         break
#     result = predict_news(user_input)
#     print(f"Result: {result}")