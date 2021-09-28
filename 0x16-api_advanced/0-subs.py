#!/usr/bin/python3

import requests as req


def number_of_subscribers(subreddit):
    '''returns the number of subscribers for a given subreddit'''
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    reddit = req.get(url, headers={'User-agent': 'your bot 0.1'}).json()

    return reddit['data']['subscribers']
