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

user = api.get_user('aragon_sharick')
print(user)