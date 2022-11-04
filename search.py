import configparser
import tweepy
import json
import pandas as pd
import dash
import plotly.express as px
from tweepy.auth import OAuthHandler
from dash import dcc, html
from dash.dependencies import Input, Output, State

#Traemos las keys del config
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
acces_token_secret = config['twitter']['access_token_secret']

#Damos las credencias a tweepy
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token (access_token, acces_token_secret)

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

#DASH
app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
    html.H1('Busca tu palabra en tendencia'),
    html.Img(src='assets/Twitter.png'),
    ], className='banner'),

    html.Div([
        html.Label('Ingresa tu palabra empezando con un "@"'),
        dcc.Input(placeholder='@Cristiano', id="username", type='text'),
    ], className='fix_label'),

   html.Div([
        html.Button('Buscar', id='search', n_clicks=0)
    ], className='buttonBuscar'),   
   
   html.Div(
       id='basic-output',
       children='this is a result'
   )
])

@app.callback(
    Output(component_id='basic-output', component_property='children'),
    [Input(component_id='username', component_property='value')],
    [State('search', 'value')]
)

def apiSearch (id, value):
    print(id)
    users = api.search_users(q=id, count=5)
    json_str = json.dumps(users, indent=3)
    readJson = pd.read_json(json_str)
    print(readJson)
    return 'This id is awesome {}'.format(id)
 
if __name__ == ('__main__'):
    app.run_server(debug=True)