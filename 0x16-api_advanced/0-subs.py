#!/usr/bin/python3
'''Ses'''

import requests as req
from requests import status_codes


def number_of_subscribers(subreddit):
    '''returns the number of subscribers for a given subreddit'''
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    reddit = req.get(url, headers={'User-agent': 'your bot 0.1'})

    if (reddit.status_code >= 200 and reddit.status_code <= 299):
        return reddit.json()['data']['subscribers']
    return 0
