import slack_sdk
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from yaml import load, SafeLoader
from datetime import datetime, timedelta
import os

SLACK_KEY = "SlackKey"
CHANNEL_KEY = "ChannelKey"


def fetch_slack_messages(config: str):
    with open(config) as cfg:
        d = load(cfg, SafeLoader)
        if SLACK_KEY not in d or CHANNEL_KEY not in d:
            print("Error: 'SlackKey' not found in configs")
            return False

        client = WebClient(token=d[SLACK_KEY])
        last_time = datetime.now() - timedelta(hours=3, minutes=0)
        print(d[SLACK_KEY], d[CHANNEL_KEY])

        return client.conversations_history(oldest=last_time.timestamp(), channel=d[CHANNEL_KEY])

def post_slack_messages(config: str, msg: str, channel: str="general"):
    with open(config) as cfg:
        d = load(cfg, SafeLoader)
        if SLACK_KEY not in d:
            print("Error: 'SlackKey' not found in configs")
            return False
    
    client = WebClient(token=d[SLACK_KEY])

    try:
        response = client.chat_postMessage(
        channel=channel,
        text=msg
        )
    except SlackApiError as e:
        assert e.response["error"]
        return False

    return True

# fetch_slack_messages("%s/config/slack.yaml"% os.getcwd())