"""Retrive tweets and users then create embeddings and populate DB"""
from os import getenv
import tweepy
import spacy
from .data_model import DB, Tweet, User

twitter_api_key = getenv("TWITTER_API_KEY")
twitter_api_secret = getenv("TWITTER_API_SECRET")
twitter_auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
twitter_api = tweepy.API(twitter_auth)

def upsert_user(twitter_handle):
    try:
        twitter_user = twitter_api.get_user(twitter_handle)
        if User.query.get(twitter_user.id):
            db_user = User.query.get(twitter_user.id)
        else:
            db_user = User(id=twitter_user.id, name=twitter_handle)
        DB.session.add(db_user)

        user_tweets = twitter_user.timeline(count=200, exclude_replies=True,
        include_rts=False, tweet_mode="extended")

        for tweet in user_tweets:
            db_tweet = Tweet(id=tweet.id, text=tweet.full_text)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        raise e
    else:
        DB.session.commit()
