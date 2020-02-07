#!/usr/bin/python3
""" Query the Reddit API and returns the number of subscribers """

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ Return the number of subscribers for a given subreddit"""
    header = {'User-Agent': ''}
    reddit = requests.get('https://www.reddit.com/r/{}/about.json'
                          .format(subreddit), headers=header)
    if reddit.status_code != 200:
        return 0
    return reddit.json().get('data', {}).get('subscribers', 0)
