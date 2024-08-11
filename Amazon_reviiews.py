import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from PIL import Image, ImageOps
import seaborn as sns
import numpy as np
from wordcloud import WordCloud, STOPWORDS


Inno = Image.open("Inno (2).jpeg")
st.image(Inno)
# Correct file paths for images

Amazon = Image.open("Amazon.jpeg")
st.image(Amazon)
# Display the image using Streamlit's image function
#st.image(vk, use_column_width=False)
st.title("Amazon Reviews Classification")

# Load the CSV file
df = pd.read_csv(r"C:\Users\RAGHAVENDRA KUMAR\ML\NLP\VK_final.csv")



# Load the pre-trained model and vectorizer
model_path = r"C:\Users\RAGHAVENDRA KUMAR\ML\NLP\amazon_reviews.pkl"
vectorizer_path = r"C:\Users\RAGHAVENDRA KUMAR\ML\NLP\amazon_tfidf.pkl"

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, 'rb') as vectorizer_file:
    Bagw = pickle.load(vectorizer_file)

# Input review from user
comment = st.text_input("Enter your Review:")

# Transform the input review using the loaded vectorizer
if st.button("Submit"):
    data = Bagw.transform([comment]).toarray()
    pred = model.predict(data)[0]
    star1=Image.open("1 star.jpg")
    star2=Image.open("2 star.jpg")
    star3=Image.open("3star.jpg")
    star4=Image.open("4 star.jpg")
    star5=Image.open("5star.jpg")
    if pred==1:
        st.image(star1)
    elif pred==2:
        st.image(star2)
    elif pred==3:
        st.image(star3)
    elif pred==4:
        st.image(star4)
    else:
         st.image(star5)





