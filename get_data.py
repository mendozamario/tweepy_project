import configparser
import tweepy 
import json
import mysql.connector
import pandas as pd
from tweepy.auth import OAuthHandler

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
acces_token_secret = config['twitter']['access_token_secret']

username = config['mysql']['username']
password = config['mysql']['password']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token (access_token, acces_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

myConnection = mysql.connector.connect(host='localhost', user=username, passwd=password, database='mys')

def saveUser(username) :
    user = visualizeUsers(username)
    name=""
    screen_name=""
    location=""
    id=0
    friends_count=0
    followers_count=0
    listed_count=0
    favourites_count=0
    statuses_count=0
    verfied=False

    id=int(user["id"])
    name=str(user["name"])
    screen_name=str(user["screen_name"])
    location=str(user["location"])
    followers_count=int(user["followers_count"])
    friends_count=int(user["friends_count"])
    listed_count=int(user["listed_count"])
    favourites_count=int(user["favourites_count"])
    statuses_count=int(user["statuses_count"])
    verfied=bool(user["verified"])

    myCursor = myConnection.cursor()
    sql = "INSERT INTO usuario (id, username, screen_name, location, followers_count, friends_count, listed_count, favourites_count, statuses_count, verified) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (id, name, screen_name, location, followers_count, friends_count, listed_count, favourites_count, statuses_count, verfied)
    myCursor.execute(sql, values)

    myConnection.commit()
    print("1 record inseted, ID:", myCursor.lastrowid)

def getUsers() :
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM usuario")
    myResult = myCursor.fetchall()

    for x in myResult : 
        print(x)

def visualizeUsers(username) :
    user = api.get_user(screen_name = username)

saveUser("tokischa_")
    
