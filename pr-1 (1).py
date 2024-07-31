import nltk
import os
from PIL import Image
from nltk.sentiment import SentimentIntensityAnalyzer
  #Initialize the SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    #Perform sentiment analysis
    sentiment_scores = sid.polarity_scores(text)
    
    #Classify sentiment based on compound score
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'
     #Example text data:
Social_media_post = "Your content always brightens my day!Keep spreading joy and inspiration!."
Restaurant_review = "The Overall Ambiance of the Resturant was lacking.It didn't feel inviting or welcoming!."
Project_feedback="Overall,the project achieved its objectives,but there were minor setbacks along the way."




     #Here we will Analyze sentiment
print("Social Media Post Sentiment:", analyze_sentiment(Social_media_post))
print("Restaurant Review Sentiment:", analyze_sentiment(Restaurant_review))
print("Project feedback Sentiment:", analyze_sentiment(Project_feedback))


