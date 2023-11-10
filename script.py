import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

twitch_user = os.getenv('TWITCH_USER')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
webhook_url = os.getenv('WEBHOOK_URL')

auth_params = {'client_id': client_id, 'client_secret': client_secret, 'grant_type' : 'client_credentials'}
try:
  auth_response = requests.post('https://id.twitch.tv/oauth2/token', data=auth_params)
  print('Authenticated to Twitch')
except requests.exceptions.RequestException as e:
  raise SystemExit(e)

access_token = auth_response.json()['access_token']
headers= {'Authorization' : f'Bearer {access_token}', 'Client-Id' : client_id}
stream_params = {'user_login': twitch_user}

try:
  response = requests.get('https://api.twitch.tv/helix/streams', headers=headers, params=stream_params)
  print(f'Got stream details for {twitch_user}')
except requests.exceptions.RequestException as e:
  raise SystemExit(e)

data = response.json()['data'][0]

game_name = data['game_name']
title = data['title']
thumbnail_url = data['thumbnail_url']
timestamp = time.time_ns()

#append timestamp to thumbnail url to prevent caching of image
url_ts = f'{thumbnail_url.format(width=320, height=180)}?ts={timestamp}'

discord_body = {
  'content': f'@everyone {twitch_user} is now LIVE on Twitch! See you in chat! :rocket:',
  'embeds': [
    {
      'title': title,
      'url': f'https://www.twitch.tv/{twitch_user}',
      'color': 9174960,
      'image': {
        'url': url_ts
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

try:
  discord_response = requests.post(webhook_url, json=discord_body)
  print(f'Posted to Discord {discord_response}')
except requests.exceptions.RequestException as e:
  raise SystemExit(e)
