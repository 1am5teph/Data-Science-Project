# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:56:40 2016

@author: Lil Puter
"""
import praw
import pickle
import pandas
from datetime import datetime
# import json
# import sqlite3

r = praw.Reddit(user_agent = 'Post Subject on r/Portland')
# works
# username = input('username: ')
# password = input('password: ')
# r.login(username, password, disable_warning=True)

# pick a subreddit
print('hello! i will compile reddit submissions.')
subreddit = r.get_subreddit(input('pick a subreddit: '))

# create post dictionary with title, points, and timestamp
postdic = {}

# Get New Subreddit Posts
for post in subreddit.get_new(limit = 5):
    # Get Post ID
    postID = str(post.id)
    # Get Post Title and Total Points
    titlePoints = r.get_submission(submission_id = postID)
    # print(titlePoints)

    # Tag Karma and Title for titlePoints
    stringTitle = str(titlePoints)
    karma, title = stringTitle.split(":: ")
    title = str(title)
    # Get Post Timestamp
    submissionTimeStamp = datetime.fromtimestamp(titlePoints.created_utc)
    # print(SubmissionTimeStamp)

    #append to post dictionary
    postdic[title] = str(submissionTimeStamp), karma


def getComments():
    #Get Post Comments
    CommentID = praw.helpers.flatten_tree(titlePoints.comments)
    for comment in CommentID:
        commentText = str(comment.body)
        # print(commentText)
        # Get Comment Timestamp
        commentTimeStamp = str(datetime.fromtimestamp(comment.created_utc))
        # print(CommentTimeStamp)

        # append to post dictionary
        postdic[title] = commentTimeStamp, commentText
        return(postdic)

# Create a DataFrame
data = pandas.DataFrame.from_dict(postdic,orient = 'index')
# Dataframe uses PostTitle as index
# Creates 0, n.... index
data = data.reset_index()
data.columns = (['PostTitle', 'TimeStamp', 'Karma'])
print(data)

# pickle it
data_file = "data-file"
fileObject = open(data_file, 'wb')
pickle.dump(data, fileObject)
fileObject.close()

# dump pickle
# dic = pickle.load(open("data-file", "rb"))

# create list of words
wordList = {}

for i in df['PostTitle']:
    postString = str(i.lower())
    words = postString.split()
    for w in words:
        #ignore 'the', 'and', 'a', 'an'
        if w == 'the'|'an':
            continue
        else:
            wordList.append(w)




#
#    #get title submissions for past year
#    #TO-DO: use user input in future
#content = r.get_submissions(page_url = 'reddit.com/r/portland', limit = 10)
#submissions =r.search(query = 'cat', limit = 10)
#print(submissions)
#create dictionary
    #Keywords: homeless, rent, gentrification, california, market, dodg, cat
