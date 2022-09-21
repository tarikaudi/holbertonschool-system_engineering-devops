#!/usr/bin/python3
"""comment for the chekcer"""

import requests


def number_of_subscribers(subreddit):
    """get def fun"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request = requests.get(url, headers={'User-agent': 'your bot 0.1'}).json()
    try:
        subs = r["data"]["subscribers"]
        return subs
    except:
        return 0
