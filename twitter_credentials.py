# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:31:01 2019

@author: abhis
"""

import json

# create a dictionary to store your twitter credentials

twitter_cred = dict()

# Enter your own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = '8InsjGGJGkPl1Kt2jrEoMm3BD'
twitter_cred['CONSUMER_SECRET'] = 'SDVWDeItox0YLcnaa4TKKrqftDIWUxN6cvjqPtoSdk9QMUqS1C'
twitter_cred['ACCESS_KEY'] = '951883783-dI6kw9ZLG1Y5QUnydeoaTTmX6fhZ4S45RRYOWr93'
twitter_cred['ACCESS_SECRET'] = 'R7IozqGOUOU9CxtGKz277J15Cb0xP5LCFnvLkEq2k85eF'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public

with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)