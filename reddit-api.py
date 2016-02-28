# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:56:40 2016

@author: Lil Puter
"""
# import json
# import requests
#
# # Get Data
# r = requests.get("https://reddit/r/portland/api/")
# r.text
# #
# ## Convert to dictionary
# data = json.loads(r.text)
# print(data)

import praw
import sys
import json

submissions = []

r = praw.Reddit(user_agent='Post Subject on r/Portland')
#works
#username = input('username: ')
#password = input('password: ')
#r.login(username, password, disable_warning=True)

#pick a subreddit
print('hello! i will compile reddit submissions.')
subreddit = r.get_subreddit(input('pick a subreddit: '))
posts = []

for post in subreddit.get_new(limit=2):
    # DON"T USE
    # title = str(post.title)
    # Receiving encoding errors on some posts - must contain unrecognized character
    # print(title.encode(sys.stdout.encoding, errors = 'replace'))

    postID = str(post.id)
    posts.append(postID)
    titlePoints = r.get_submission(submission_id = postID)
    print(titlePoints)
    print(str(titlePoints.created_utc))
    CommentID = praw.helpers.flatten_tree(titlePoints.comments)
    for comment in CommentID:
        print(str(comment.body))
        print(str(comment.created_utc))

    # DON"T USE
    # postComments = submissionText.comments # this gives me comments object key
    # print(postComments) # this gives me comments object key

# get date
# for post in posts:
#     dateTime = r.get_created_utc()
#     print(dateTime)


# for i, submission in enumerate(subreddit.get_hot(limit=10)):
#     submissions.append(r.get_submission(submission_id = submission.id))
# print(submissions)

##create dataset for specific time period
#    #need title, dates, submissions, and count
#
#    #get title submissions for past year
#    #TO-DO: use user input in future
#content = r.get_submissions(page_url = 'reddit.com/r/portland', limit = 10)
#submissions =r.search(query = 'cat', limit = 10)
#print(submissions)
#create dictionary
    #Keywords: homeless, rent, gentrification, california, market, dodg, cat
