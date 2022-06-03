import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

twitch_user = os.getenv('TWITCH_USER')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
webhook_url = os.getenv('WEBHOOK_URL')

print('Authenticating to Twitch')

auth_params = {'client_id': client_id, 'client_secret': client_secret, 'grant_type' : 'client_credentials'}
auth_response = requests.post('https://id.twitch.tv/oauth2/token', data=auth_params)

access_token = auth_response.json()['access_token']

print('Getting stream info')
headers= {'Authorization' : f'Bearer {access_token}', 'Client-Id' : client_id}
stream_params = {'user_login': twitch_user}
response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=stream_params)
data = response.json()['data'][0]

print('Posting message to Discord')
game_name = data['game_name']
title = data['title']
random = time.time_ns()

discord_body = {
  'content': f'@everyone {twitch_user} is now LIVE on Twitch! See you in chat! :rocket:',
  'embeds': [
    {
      'title': title,
      'url': f'https://www.twitch.tv/{twitch_user}',
      'color': 9174960,
      'image': {
        'url': f'https://static-cdn.jtvnw.net/previews-ttv/live_user_{twitch_user}-320x180.jpg?rnd={random}'
      },
      'fields': [
        {
          'name': ':joystick: Game',
          'value': f'{game_name}\u200B',
          'inline': 'true'
        }
      ]
    }
  ]
}

discord_response = requests.post(webhook_url, json=discord_body)
print(discord_response)