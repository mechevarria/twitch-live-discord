import requests
import os
from dotenv import load_dotenv

load_dotenv()

twitch_user = os.getenv('TWITCH_USER')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
webhook_url = os.getenv('WEBHOOK_URL')

print('Authenticating to Twitch')

params = {'client_id': client_id, 'client_secret': client_secret, 'grant_type' : 'client_credentials'}
response = requests.post('https://id.twitch.tv/oauth2/token', data=params)

access_token = response.json()['access_token']

print('Getting stream info')
headers= {'Authorization' : f'Bearer {access_token}', 'Client-Id' : client_id}
params = {'user_login': twitch_user}
response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=params)
data = response.json()['data'][0]

print('Posting message to Discord')
# not complete
game_name = data['game_name']
id = data['id']
title = data['title']