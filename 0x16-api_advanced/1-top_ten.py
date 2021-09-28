#!/usr/bin/python3

import requests as req


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts for a given subreddit'''
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    reddit = req.get(url, headers={'User-agent': 'your bot 0.1'})

    if (reddit.status_code >= 200 and reddit.status_code <= 299):
        reddict = reddit.json()
        childrenList = reddict.get('data').get('children')
        for i in range(0, len(childrenList)):
            print(childrenList[i].get('data').get('title'))
        return
    return print('None')
