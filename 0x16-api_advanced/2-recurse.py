#!/usr/bin/python3
'''returns a list containing the titles of all hot articles'''

import requests as req


def recurse(subreddit, hot_list=[]):
    '''prints the titles of the first 10 hot posts for a given subreddit'''
    return myRecursion(subreddit, hot_list, '')


def myRecursion(subreddit, hot_list, page):
    '''my real recursion'''
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?after=' + page
    headers = {'User-agent': 'your bot 0.1'}
    reddit = req.get(url, headers=headers, allow_redirects=False)

    if (reddit.status_code >= 200 and reddit.status_code <= 299):
        hotContent = reddit.json().get('data').get('children')
        nextPage = reddit.json().get('data').get('after')

        for post in hotContent:
            hot_list.append(post.get('data').get('title'))

        if (nextPage is not None):
            myRecursion(subreddit, hot_list, nextPage)

        return hot_list
    else:
        return None
