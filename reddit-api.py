# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:56:40 2016

@author: Lil Puter
"""

#import json
#import requests
#
## Get Data
#r = requests.get("https://github.com/r/portland/api/subreddits")
#r.text
#
## Convert to dictionary
#data = json.loads(r.text)
#print(data)

import praw
r = praw.Reddit(user_agent='Post Subject on r/Portland')

print('hello!')
subreddit = r.get_subreddit(input('pick a subreddit: '))
print('the top 5 hot posts are: ')
for post in subreddit.get_hot(limit = 5):
    print(post)

