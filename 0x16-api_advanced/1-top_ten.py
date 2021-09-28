#!/usr/bin/python3

import requests as req


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts for a given subreddit'''
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    reddit = req.get(url, headers={'User-agent': 'your bot 0.1'}).json()

    return reddit['data']['subscribers']
