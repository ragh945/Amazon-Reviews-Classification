# Amazon Reviews Classification
## Project Objective
The objective of this project is to develop a classification model to predict the rating of Amazon reviews based on their textual content. The ratings range from 1 to 5 stars. This model utilizes Natural Language Processing (NLP) techniques to analyze the comments and predict the corresponding rating.

# Deployment Link : https://amazon-reviews-classification-srlubcdcwkhzyctxplsqvu.streamlit.app/


![Amazon_r](https://github.com/user-attachments/assets/0555c3a7-b8d8-49e2-a37c-10db796bfa51)



## Libraries Used
- Streamlit: For building the interactive web application.
- Pickle: For loading pre-trained models and vectorizers.
- Pandas: For data manipulation and processing.
- Matplotlib & Seaborn: For data visualization (optional).
- WordCloud: For visualizing the most frequent words in the reviews.
- Scikit-learn: For machine learning algorithms and text vectorization.
- Pillow: For handling image processing.

## Features
- Text Input: Users can enter an Amazon review text.
- Rating Prediction: The model predicts the rating based on the review text.
- Visual Output: Displays an image corresponding to the predicted rating (1 to 5 stars).

## Model Details
- Algorithm: Random Forest Classifier
- Text Vectorization: TF-IDF Vectorizer is used to convert text data into numerical features.

## Data Preprocessing
### Text Preprocessing:
- Tokenization: Splitting text into individual words.
- Removal of stop words: Filtering out common words that do not contribute to the meaning of the review.
- Lowercasing: Converting all text to lowercase to maintain uniformity.
- Stemming/Lemmatization: Reducing words to their base or root form.

## TF-IDF Vectorization:
- Transforms text data into numerical feature vectors that represent the importance of words in the reviews relative to the corpus.

## Train-Test Split:
- The dataset is split into training and testing subsets to evaluate the performance of the model.


# Conclusion:
This project demonstrates the application of Natural Language Processing (NLP) for classifying Amazon reviews based on their textual content. By leveraging a Random Forest Classifier and TF-IDF Vectorization, the model is able to accurately predict review ratings from 1 to 5 stars. The interactive Streamlit application provides a user-friendly interface for real-time classification, making it easy to analyze and visualize sentiment in reviews.
