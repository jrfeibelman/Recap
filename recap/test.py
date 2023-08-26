from slack import WebClient
from slack.errors import SlackApiError
from yaml import load, SafeLoader
from datetime import datetime, timedelta
import os

SLACK_KEY = "SlackKey"
CHANNEL_KEY = "ChannelKey"

with open("%s/config/slack.yaml" % os.getcwd()) as cfg:
    d = load(cfg, SafeLoader)
    if SLACK_KEY not in d or CHANNEL_KEY not in d:
        print("Error: %s not found in configs" % SLACK_KEY)

    client = WebClient(token=d[SLACK_KEY])

    # print(client.team_info())
    print(client.admin_users_list(team_id="T05PLEQHFN1"))