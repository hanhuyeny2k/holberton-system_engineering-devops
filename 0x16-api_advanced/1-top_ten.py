#!/usr/bin/python3
""" Print the titles of the first 10 hot posts listed for a given subreddit """

import requests
from sys import argv


def top_ten(subreddit):
    """ Print the first top 10 posts """
    header = {'User-Agent': ''}
    param = {'limit': 10}
    reddit = requests.get('https://www.reddit.com/r/{}/hot.json'
                          .format(subreddit), headers=header, params=param,
                          allow_redirects=False, timeout=10)
    if reddit.status_code != 200:
        print('None')
    else:
        for top_10 in reddit.json().get('data', {}).get('children', []):
            print(top_10.get('data', {}).get('title'))
