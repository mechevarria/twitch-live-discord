# twitch-live-discord

Python script to authenticate against the [Twitch API](https://dev.twitch.tv/docs/api/), get live user details and then post a rich text message to a channel in [Discord](https://discord.com/developers/docs/reference). The reason I built this instead of using a bot is that most bots do not add a random number to the preview URL, resulting in a [cached image in Discord](https://discuss.dev.twitch.tv/t/feature-request-one-small-change-that-could-fix-the-discord-webhook-embed-cached-image-issues/27477)

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

```properties
TWITCH_USER="twitch_streamer_name"
CLIENT_ID="<your twitch app client id"
CLIENT_SECRET="<your twitch dev secret>"
WEBHOOK_URL="https://discord.com/api/webhooks/<REST OF THE URL>
```

## Execute the script

* Run the script to with the following command.

```bash
python3 script.py
```

* Example output in Discord
![discord](screenshots/discord.png)