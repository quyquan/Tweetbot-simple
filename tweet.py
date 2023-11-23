import os
import tweepy
import time

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def tweet_every_hour():
    while True:
        # Get the current hour
        hour = datetime.datetime.now().hour

        # Tweet if the current hour is on the hour
        if hour % 1 == 0:
            tweet_text = "This is an hourly tweet!"
            api.update_status(tweet_text)

        # Wait for one hour before tweeting again
        time.sleep(3600)

if __name__ == "__main__":
    tweet_every_hour()
