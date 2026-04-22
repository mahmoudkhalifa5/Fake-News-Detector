# # predict.py

# import pickle
# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer

# nltk.download('stopwords')

# model = pickle.load(open("fake_news_model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# stop_words = set(stopwords.words('english'))
# stemmer = PorterStemmer()

# def clean_text(text):
#     text = text.lower()
#     text = re.sub(r'[^a-zA-Z\s]', '', text)
#     words = text.split()
#     words = [stemmer.stem(w) for w in words if w not in stop_words]
#     return ' '.join(words)

# def predict_news(text):
#     cleaned = clean_text(text)
#     vec = vectorizer.transform([cleaned])
#     pred = model.predict(vec)[0]
#     return "FAKE ❌" if pred == 1 else "REAL ✅"

# # interactive
# while True:
#     news = input("Enter news: ")
#     if news == "exit":
#         break
#     print(predict_news(news))