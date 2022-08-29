import re 
import tweepy 
import nltk
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
nltk.download('punkt')   
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from tweepy import OAuthHandler 
from textblob import TextBlob

#twitter api keys
APIKEY = 'nuZKOtiKO0LXer4gp2AQ9VlbZ'
APISECRET = 'HOrPTUsFOOn4jOBEJdDURDWqwZdHNR6GnbQ9c6OsTvdOhiisl2'
ACCESSTOKEN = '1485731753620742145-264yiXQXQAI0IhpLZpX5XlUVJFH9n1'
ACCESSTOKENSECRET = 'MFbUIFfAjOLECu9cFOIg8hXu4OLgBOjykmWj9jx0BZGka'

auth = tweepy.OAuthHandler(APIKEY, APISECRET)
auth.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)

api = tweepy.API(auth) #api allows access to twt functionality

tweets = api.search_tweets('Ariana Grande')

for tweet in tweets:
    # tweet = re.sub(r'(@[A-Za-z0-9_]+)', '', tweet) #remove mentions
    # tweet = re.sub('http://\S+|https://\S+', '', tweet) #remove links
    # tweet = re.sub(r'[^\w\s]', '', tweet) #remove punctuation
    # tweetTokens = word_tokenize(tweet)
    # tweet = [word for word in tweetTokens if not word in stopwords.words()] #remove stopwords
    # tweet = ' '.join(tweet)
    print(tweet.text)
    blob = TextBlob(tweet.text)
    print(blob.sentiment)