import configparser
import tweepy 
import pandas as pd
from tweepy.auth import OAuthHandler

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
acces_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token (access_token, acces_token_secret)

api = tweepy.API(auth)


def exportUserTimeline(username):
    data_list = []

    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username, exclude_replies = True, include_rts = False, tweet_mode = 'extended').items():
        data_list.append([tweet.full_text, tweet.created_at, tweet.favorite_count, tweet.retweet_count])
        
    data_list = pd.DataFrame(data_list, columns = ["Text", "Created At", "Likes", "Retweets"])

    data_list.to_csv("user_timeline.csv")
    
exportUserTimeline('aragon_sharick')