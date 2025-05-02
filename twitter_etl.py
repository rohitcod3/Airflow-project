import tweepy
import pandas as pd
from datetime import datetime
import s3fs
from dotenv import load_dotenv
import os

load_dotenv()

def run_twitter_etl():

    bearer_token = os.getenv("BEARER_TOKEN")

    client = tweepy.Client(bearer_token=bearer_token)

    user_response = client.get_user(username='rohit_rr1')
    print(user_response)
    user_id = user_response.data.id

    tweets_response = client.get_users_tweets(
        id=user_id,
        max_results=100, 
        tweet_fields=['created_at', 'text']
    )

    tweet_data = [{
        'created_at': tweet.created_at,
        'text': tweet.text
    } for tweet in tweets_response.data]

    df = pd.DataFrame(tweet_data)

    print(df.head())

    tweet_list = []

    username = user_response.data.username

    for tweet in tweets_response.data:
        refined_tweet = {
            "user": username,
            "text": tweet.text,
            "created_at": tweet.created_at.isoformat() if tweet.created_at else None
        }
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://rohiiit-airflow-bucket/my_twitter_data.csv")


    