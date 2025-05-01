import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
from dotenv import load_dotenv
import os


load_dotenv()

access_key = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")


auth = tweepy.OAuthHandler(access_key, access_secret)

auth.set_access_token(consumer_key, consumer_secret)

api = tweepy.API(auth)