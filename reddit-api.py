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
import sys

r = praw.Reddit(user_agent='Post Subject on r/Portland')
r.config.decode_html_entities = True

print('hello!')
subreddit = r.get_subreddit(input('pick a subreddit: '))
for post in subreddit.get_hot(): 
    posts = post.title
    print(posts.encode(sys.stdout.encoding, errors = 'ignore'))


      
# Receiving encoding errors on some posts - must contain unrecognized character
    


#search subreddit for time period
