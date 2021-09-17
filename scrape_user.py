# Module imports 
import tweepy
import time
import pandas as pd
import numpy as np
import json
import time
from random import randint, random
from googlesearch import search as gsearch
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import pathlib
import os
from dotenv import load_dotenv

# name the file we want
env_file_name = 'lrhf97_twit_cred.env'
parent_dir = pathlib.Path.cwd().parent

env_path = parent_dir.joinpath(env_file_name)

load_dotenv(env_path)
test_cred = os.getenv("test_cred")

api_key = os.getenv("API_KEY")
secret_key = os.getenv("API_SECRET")
access_token = ''
secret_token = ''

def authenticate(api_key, secret_key, access_token, secret_token):

    auth = tweepy.OAuthHandler(api_key, secret_key)
    auth.set_access_token(access_token, secret_token)
    api = tweepy.API(auth, 
                     wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True)
  
    return api


api = authenticate(api_key, secret_key, access_token, secret_token)