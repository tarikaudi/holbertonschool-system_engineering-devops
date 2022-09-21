#!/usr/bin/python3
"""comment for the checker"""

import requests


def recurse(subreddit, tlist=[], pos=0):
    """def recursive"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url, headers={'User-agent': 'your bot 0.1'},
                     allow_redirects=False)
    if request.status_code != 200:
        return None
    try:
        tlist.append(request.json()['data']['children'][pos]['data']['title'])
    except IndexError:
        return tlist
    return (recurse(subreddit, tlist, pos+1))
