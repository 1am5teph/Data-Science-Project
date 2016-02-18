# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:56:40 2016

@author: Lil Puter
"""

import json
import requests

# Get Data
r = requests.get("https://github.com/r/portland/api/subreddits_by_topic")
r.text

# Convert to dictionary
data = json.loads(r.text)