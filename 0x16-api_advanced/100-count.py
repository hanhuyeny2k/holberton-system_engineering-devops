#!/usr/bin/python3
""" Parse the title of all hot articles and prints a sorted count """

import requests
from sys import argv


def count_words(subreddit, word_list):
    """ Count words """
    header = {'User-Agent': ''}
    params = {'limit': 100}
    if after:
        params['after'] = after
    reddit = requests.get('https://www.reddit.com/r/{}/hot.json'
                          .format(subreddit), headers=header, params=params)
    if reddit.status_code != 200:
        return hot_list or None
    data = reddit.json().get('data', {})
    for i in data['children']:
        hot_list.append(i['data']['title'])
    if not hot_list:
        return hot_list
    after = data.get('after', '')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
