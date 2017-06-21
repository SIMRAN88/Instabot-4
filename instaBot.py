# Importing the APP_ACCESS_TOKEN
from access_token import APP_ACCESS_TOKEN  # <<access_token is in the scope of basic, public_content, likes, comments.>>>

# Importing Requests library to make network requests
import requests
# Importing urlib to download the posts
import urllib

# Importing termcolor for a colorful output
from termcolor import colored

# Importing TextBlob to delete negative comments
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

import matplotlib.pyplot as plt
import numpy as np



# Base URL common for all the requests in the file.
BASE_URL = 'https://api.instagram.com/v1/'

# *****************************************
# Function declaration to get your own info
# *****************************************
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()       # GET call to fetch self information

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print(colored('Full Name    : %s' % (user_info['data']['full_name']), 'red'))
            print(colored('Username     : %s' % (user_info['data']['username']),'red'))
            print(colored('UserId       : %s' % (user_info['data']['id']), 'red'))
            print(colored('Followed By  : %s' % (user_info['data']['counts']['followed_by']),'red'))
            print(colored('Follows      : %s' % (user_info['data']['counts']['follows']),'red'))
            print(colored('Total Posts  : %s' % (user_info['data']['counts']['media']),'red'))

            if user_info['data']['website'] != '':      # Website of the user is given
                print(colored('Website      :%s' % (user_info['data']['website']), 'blue'))
            if user_info['data']['bio'] != '':          # Bio of the user is given
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
    user_info = requests.get(request_url).json()       # GET call to fetch user for the information

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            user_id = user_info["data"][0]["id"]
            return user_id  # To Return user's id
        else:
            return None
    else:
        print 'Status code other than 200 received!'

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
    user_info = requests.get(request_url).json()       # GET call to fetch user for the information
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print(colored('Full Name    : %s' % (user_info['data']['full_name']), 'red'))
            print(colored('Username     : %s' % (user_info['data']['username']),'red'))
            print(colored('UserId       : %s' % (user_id), 'red'))
            print(colored('Followed By  : %s' % (user_info['data']['counts']['followed_by']),'red'))
            print(colored('Follows      : %s' % (user_info['data']['counts']['follows']),'red'))
            print(colored('Total Posts  : %s' % (user_info['data']['counts']['media']),'red'))

            if user_info['data']['website'] != '':      # Website of the user is given
                print(colored('Website      :%s' % (user_info['data']['website']), 'blue'))
            if user_info['data']['bio'] != '':           # Bio of the user is given
                print(colored('Bio          :%s' % (user_info["data"]["bio"]), 'blue'))
            print("<>@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@<>")
            print (colored("~~~~~~~~~~~~~~~~~~The user is a social bird~~~~~~~~~~~~~~~~~~~~~.", "blue"))
            print("<>@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@<>")
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

# **************************************************
# Function declaration to get recent post of yourself
# **************************************************
def get_own_recent_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()           # GET call to fetch details of own recent post

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            if own_media['data'][0]['caption']['text'] != '':
                print(colored("Caption:",'yellow')),
                print (colored(own_media['data'][0]['caption']['text'],'red'))   # Fetching the caption of the post
                print(colored("Image Name:", "blue")),
                print image_name
            else:
                print(colored("Image Name","blue")),
                print image_name
            print 'The post has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

# ****************************************************************
# Function declaration to get the recent post of a user by username
# ****************************************************************
def get_user_recent_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()       # GET call to fetch the user recent post

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            if user_media['data'][0]['caption']['text'] != '':
                print(colored("Caption:",'yellow')),
                print (colored(user_media['data'][0]['caption']['text'],'red'))
                print(colored("Image Name:", "blue")),
                print image_name
            else:
                print(colored("Image Name", "blue")),
                print image_name
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


# *******************************************************
# Get the list of recent media liked by the owner of id
# *******************************************************
def get_own_recently_liked():
    request_url = (BASE_URL + 'users/self/media/liked/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            if own_media['data'][0]['caption'] != 'None':
                print(colored("Caption:",'yellow')),
                print (colored(own_media['data'][0]['caption'],'red'))
                print(colored("Image Name:", "blue")),
                print image_name
            else:
                print(colored("Image Name","blue")),
                print image_name
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

# *************************************************************************
# Function declaration to get the ID of the recent post of a user by username
# ***************************************************************************
def get_post_id_recent(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()
        
# *******************************************************************************************************
# The function below fetches all public post starting from the most recent one published by the user using 'GET'.
# **********************************************************************************************************
def get_user_post(username):
    user_id = get_user_id(username)  # get_user_id(username) function called here to get the user's ID
    user_url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + APP_ACCESS_TOKEN
    request_user_recent_post = requests.get(user_url).json()  # GET call to fetch user's post
    return request_user_recent_post

# ***************************************************************************
# Function declaration to make delete negative comments from the recent post
# ***************************************************************************
def delete_negative_comment(insta_username):
    media_id = get_post_id_recent(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            # Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (
                        media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'


# *********************************************************
# Start the Bot
# **********************************************************

def start_bot():
    print (colored(('-' *100), 'red'))
    print(colored(("_/\_  "*5),'red')),
    print (colored("=========Welcome to InstaBOT!==========",'cyan')),
    print(colored(("_/\_  " * 5), 'red'))
    print (colored(('-' *100),'red'))
    print '\n'
    print(colored("<>@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SELF INFO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@<>","green"))
    self_info()
    print "<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"
    print (colored("<>@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~USERS INFO~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@<>","red"))
    print "Get a users information"
    user_name = raw_input("Enter the name of username to display the info: rohittm or sarthaknegi3181 or frozenfire8888:- ")
    get_user_info(user_name)

    print"\n"
    choice = 'yes'
    while choice != 'no':
        print '\n'
        print "What would you like to do further?"
        print(colored("1:To Like a post of your choice of the user","magenta"))
        print(colored("2:To Comment on a post(not more than 200) of your choice of the user","magenta"))
        print(colored("3:To Search a word in the comment in the post of your choice of the user","magenta"))
        print(colored( "4:To Delete the negative comment from a recent post.","magenta"))
        print(colored("5:To Get your own recent post","magenta"))
        print(colored("6:To Get the recent post of a user by username","magenta"))
        print(colored("7:To Get your recently liked media","magenta"))
        print(colored("8:To determine images shared with a particular hash tag and plot using malplotlib.","magenta"))
        print "\n"
        option = int(raw_input("Your option: "))
        print "<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"
        if option not in range(1, 10):
            print"Invalid operation \nPlease try again!"
        elif option in range(1, 4):
            print "Which post you would wish to choose :"
            print "press 1 for the one with the least popular of it"
            print "press 2 for the one which has been recently uploaded "
            print "press 3 for the one which is the most popular"
            if option == 1:
                print "press 4 to like all post"
            post_select = int(raw_input("Your option: "))
            if option == 1:
                user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi :- ")
                if post_select in [1, 2, 3]:
                    like_user_post(user_name, option, post_select, 0)
                elif post_select == 4:
                    store = get_user_post(user_name)
                    length = len(store['data'])
                    for post in range(0, length):
                        n = post
                        like_user_post(user_name, option, 4, n)  # Here n is to give the post number.
                else:
                    print"Invalid post was chosen"
                    print "(((((((((((((((((((((((((()))))))))))))))))))))))))))))))))"
                    print" Sorry we have to perform the operatin on the most recent post then"
            else:
                if post_select not in [1, 2, 3]:
                    print"Invalid post chosen \n"
            if option == 2:
                user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181:- ")
                post_a_comment(user_name, option, post_select)
            if option == 3:
                user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181:- ")
                word_search_in_comment(user_name, option, post_select)
        if option == 4:
            user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181:- ")
            delete_negative_comment(user_name)
        if option == 5:
            get_own_recent_post()
        if option == 6:
            user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181:-")
            get_user_recent_post(user_name)
        if option == 7:
            get_own_recently_liked()
        if option == 8:
            popular_hashtag()

        print "<>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<>"
        print "Do you want to continue?? (y/n)"
        opt = raw_input().upper()
        if opt == 'Y':
            choice = 'yes'
            pass
        elif opt == 'N':
            choice = 'no'
        else:
            print "Invalid choice"
            print "Please choose between y or n:"
            opt = raw_input().upper
            if opt == 'Y':
                choice = 'yes'
                pass
            elif opt == 'N':
                choice = 'no'
            else:
                print("You again chose an invalid choice")
                print("The program will shut down")
                print("@@@@@@@@@@@THANK YOU@@@@@@@@@@@@@@@")
                print "~~~~~~~~~~~~~~~Hope you had a good experience using instaBot~~~~~~~~~~~~~~~~~~~~~~~~"
                print "For any queries contact http://www.simranraj.com"
                print "<<<<<<<<<<<<<<<<<<<<<<<<Thank You have a nice day!>>>>>>>>>>>>>>>>>>>>>>>"
                exit()
    print "~~~~~~~~~~~~~~~Hope you had a good experience using instaBot~~~~~~~~~~~~~~~~~~~~~`"
    print "For any queries contact http://www.simranraj.com"
    print "<<<<<<<<<<<<<<<<<<<<<<<<<<Thank You have a nice day!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    exit()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FUNCTION END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
start_bot()