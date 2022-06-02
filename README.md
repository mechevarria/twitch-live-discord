# twitch-live-discord

Python script to authenticate against the [Twitch API](https://dev.twitch.tv/docs/api/), get live user details and then post a rich text message to a channel in [Discord](https://discord.com/developers/docs/reference)

## Setup
* Register an application with [Twitch](https://dev.twitch.tv/). Note the `Client ID` and `Client Secret`

![twitch-app](screenshots/twitch-app.png)

* Create a [Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) in Discord. Note the `Webhook URL`

![webhook](screenshots/webhook.png)

* Make sure [python-dotenv](https://github.com/theskumar/python-dotenv) is installed
``` bash
sudo apt -y install python3-pip
pip install python-dotenv
```

* Create a `.env` file in the root directory to put the follow variables

![env](screenshots/env.png)

## Execute the script

* Run the script to with the following command
```bash
python3 script.py
```