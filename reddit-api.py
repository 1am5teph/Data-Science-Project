# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:56:40 2016

@author: Lil Puter
"""
#doesn't work
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
#works
#username = input('username: ')
#password = input('password: ')
#r.login(username, password, disable_warning=True)

#pick a subreddit
print('hello! i will compile reddit submissions.')
subreddit = r.get_subreddit(input('pick a subreddit: '))
#
##create dataset for specific time period
#    #need title, dates, submissions, and count
#
#    #get title submissions for past year
#    #TO-DO: use user input in future
for post in subreddit.get_new(): 
    title = post.title
    # print(title.encode(sys.stdout.encoding, errors = 'replace'))
    # Receiving encoding errors on some posts - must contain unrecognized character
    submission = get_submissions(post)
    print(submission)

#content = r.get_submissions(page_url = 'reddit.com/r/portland', limit = 10)    
#submissions =r.search(query = 'cat', limit = 10)
#print(submissions)
#create dictionary
    #Keywords: homeless, rent, gentrification, california, market, dodg, cat


    
    