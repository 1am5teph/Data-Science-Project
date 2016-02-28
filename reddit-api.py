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

for post in subreddit.get_new(limit=2):
    # title = str(post.title)
    postID = str(post.id)
    submissionText = r.get_submission(submission_id = postID)
    submissionComments = submissionText.comments
# Receiving encoding errors on some posts - must contain unrecognized character
    # print(title.encode(sys.stdout.encoding, errors = 'replace'))
    print(submissionText)
    print(submissionComments)



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
