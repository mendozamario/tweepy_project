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

def getUsers() :
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM usuario")
    myResult = myCursor.fetchall()

    for x in myResult : 
        print(x)

def visualizeUsers(username) :
    return api.get_user(screen_name = username)

def saveUser(username) :
    user = visualizeUsers(username)

    myCursor = myConnection.cursor()
    sql = "INSERT INTO usuario (id, username, screen_name, location, followers_count, friends_count, listed_count, favourites_count, statuses_count, verified) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (user["id_str"], user["name"], user["screen_name"], user["location"], user["followers_count"], user["friends_count"], user["listed_count"], user["favourites_count"], user["statuses_count"], user["verified"])
    myCursor.execute(sql, values)

    myConnection.commit()
    print("1 record inseted, ID:", myCursor.lastrowid)


saveUser("eduercalvo")
    
