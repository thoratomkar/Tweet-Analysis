# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:02:59 2019

@author: swats
"""

import json

# create a dictionary to store your twitter credentials

twitter_cred = dict()

# Enter your own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = '4QISguiirnzwAowHL34Taiz7J' 
twitter_cred['CONSUMER_SECRET'] = 'i9CW2VTMr6nld7fD8oZoWFYsUIiImJis9mjWzqYus4flnc6BcX'
twitter_cred['ACCESS_KEY'] = '1039651647503392768-X8cA7RoJ6Tgx2ev2PB8bCvGrhXHvTs'
twitter_cred['ACCESS_SECRET'] = '5WWCf14swIKaSead38B9PBTjC1vdSXVXPifD6nBeKzVpY'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public

with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)