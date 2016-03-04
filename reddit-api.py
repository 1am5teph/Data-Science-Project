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

# pickle it
data_file = "data-file"
fileObject = open(data_file, 'wb')
pickle.dump(postdic, fileObject)
fileObject.close()

# dic = pickle.load(open("data-file", "rb"))
dic_keys = dic.keys()


data = pandas.DataFrame(dic)
# for i in len(dic_keys):
#     dic.value
# Create database
# reddit_db = sqlite3.connect("reddit.db")
# with reddit_db:
#     cursor = reddit_db.cursor()
#     cursor.execute("""CREATE TABLE reddit_posts
#         (title text, time_stamp datetime, karma int)""")




# for k, v in postdic.items():
#     print("title: ", k)
#     print("date: ", v)
#     print("karma: ", v[1])
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
