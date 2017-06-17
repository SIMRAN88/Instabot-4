# Importing the APP_ACCESS_TOKEN
from access_token import APP_ACCESS_TOKEN

# Importing Requests library to make network requests
import requests

# Importing termcolor and colorama to get a colorful output
from colorama import init
from termcolor import colored

# To initialize the colorama
#init()

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
            print(colored('Full Name    : %s' % (user_info['data']['full_name']), 'red'))
            print(colored('Username     : %s' % (user_info['data']['username']),'red'))
            print(colored('UserId       : %s' % (user_info['data']['id']), 'red'))
            print(colored('Followed By  : %s' % (user_info['data']['counts']['followed_by']),'red'))
            print(colored('Follows      : %s' % (user_info['data']['counts']['follows']),'red'))
            print(colored('Total Posts  : %s' % (user_info['data']['counts']['media']),'red'))

            # Website of the user is given
            if user_info['data']['website'] != '':
                print(colored('Website      :%s' % (user_info['data']['website']), 'blue'))
            # Bio of the user is given
            if user_info['data']['bio'] != '':
                print(colored('Bio          :%s' % (user_info["data"]["bio"]), 'blue'))

        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

# ********************************************************
# Function declaration to get the ID of a user by username
# ********************************************************

def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    # GET call to fetch user for the information
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            user_id = user_info["data"][0]["id"]
            return user_id  # To Return user's id
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()

# **********************************************************
# Function declaration to get the info of a user by username
# **********************************************************

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print(colored('Full Name    : %s' % (user_info['data']['full_name']), 'red'))
            print(colored('Username     : %s' % (user_info['data']['username']),'red'))
            print(colored('UserId       : %s' % (user_id), 'red'))
            print(colored('Followed By  : %s' % (user_info['data']['counts']['followed_by']),'red'))
            print(colored('Follows      : %s' % (user_info['data']['counts']['follows']),'red'))
            print(colored('Total Posts  : %s' % (user_info['data']['counts']['media']),'red'))

            # Website of the user is given
            if user_info['data']['website'] != '':
                print(colored('Website      :%s' % (user_info['data']['website']), 'blue'))
            # Bio of the user is given
            if user_info['data']['bio'] != '':
                print(colored('Bio          :%s' % (user_info["data"]["bio"]), 'blue'))

        else:
            print 'User does not exist!'


    else:
        print 'Status code other than 200 received!'

def start_bot():
    while True:
        print (colored(('-' *100), 'red'))
        print(colored(("_/\_  "*5),'red')),
        print (colored("=========Welcome to InstaBOT!==========",'cyan')),
        print(colored(("_/\_  " * 5), 'red'))
        print (colored(('-' *100),'red'))
        print '\n'
        print 'Here are your menu options:'
        print "a.Get your own details"
        print "b.Get details of a user by username"
        print "c.Exit"

        choice=raw_input("Enter you choice: ")
        if choice=="a":
            self_info()
        elif choice=="b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice=="c":
            exit()
        else:
            print (colored("You chose an invisible choice.Try Again",'magenta'))
            print '\n'


start_bot()