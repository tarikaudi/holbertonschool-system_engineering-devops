#!/usr/bin/python3
"""comment for the checker"""
import requests


def top_ten(subreddit):
    """def top ten"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    request = requests.get(url, headers={"User-Agent": "Mozila/5.0"})

    res_json = res.json()
    if (res.status_code == 200):
        populares = res_json["data"]["children"]
        for post in populares:
            print(post["data"]["title"])
    else:
        print(None)
