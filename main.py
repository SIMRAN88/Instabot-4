# Importing the APP_ACCESS_TOKEN
from access_token import APP_ACCESS_TOKEN

# Importing Requests library to make network requests
import requests

# Importing termcolor and colorama to get a colorful output
from colorama import init
from termcolor import colored

# To initialize the colorama
init()

# Base URL common for all the requests in the file.
BASE_URL = 'https://api.instagram.com/v1/'

# **************************************
# Function declaration to get your own info
# **************************************

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print(colored('Username     : %s' % (user_info['data']['username']),'red'))
            print(colored('Followed By  : %s' % (user_info['data']['counts']['followed_by']),'red'))
            print(colored('Follows      : %s' % (user_info['data']['counts']['follows']),'red'))
            print(colored('Total Posts  : %s' % (user_info['data']['counts']['media']),'red'))
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

self_info()