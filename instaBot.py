# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# InstaBot 4
# version 1.0
# Description: A bot that follows your command for instagram.
# Author: Simran Raj
# Author URI: http://www.SimranRaj.com/
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Importing the APP_ACCESS_TOKEN
from access_token import APP_ACCESS_TOKEN  # <<access_token is in the scope of basic, public_content, likes, comments.>>>

# Importing Requests library to make network requests
import requests

# Importing urlib library to download the posts
import urllib

# Importing termcolor for a colorful output
from termcolor import colored

# Importing TextBlob to delete negative comments
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

# Using matplotlib library to plot no of images with popular hashtags
import matplotlib.pyplot as plt

# Base URL common for all the requests in the file.
BASE_URL = 'https://api.instagram.com/v1/'

# ***************************************************************
#          Function declaration to get your own info
# ***************************************************************
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)  #https://api.instagram.com/v1/users/self/?access_token=APP_ACCESS_TOKEN
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
            print(colored('User does not exist!','red'))
    else:
        print(colored('Status code other than 200 received!',"red"))

# ************************************************************************
#       Function declaration to get the ID of a user by username
# *************************************************************************
def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)   #https://api.instagram.com/v1/users/search?q=insta_username&access_token=APP_ACCESS_TOKEN
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()       # GET call to fetch user for the information

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            user_id = user_info["data"][0]["id"]
            return user_id  # To Return user's id
        else:
            return None
    else:
        print(colored('Status code other than 200 received!','red'))

# ***************************************************************************************
#             Function declaration to get the info of a user by username
# ****************************************************************************************
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)       # Calling the function get_user_id to get a user_id
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
            print (colored("~~~~~~~~~~~~~~~~~~~~~~The user is a social bird~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.", "blue"))
            print("<>@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~@<>")
        else:
            print(colored('User does not exist!',"red"))
    else:
        print(colored('Status code other than 200 received!',"red"))

# ****************************************************************************
#         Function declaration to get recent post of yourself
# *****************************************************************************
def get_own_recent_post():
                    #  https://api.instagram.com/v1/users/self/media/recent/?access_token=APP_ACCESS_TOKEN
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
            print(colored('The post has been downloaded!',"green"))
        else:
            print(colored('Post does not exist!',"red"))
    else:
        print(colored('Status code other than 200 received!',"red"))

# **********************************************************************************************
#              Function declaration to get the recent post of a user by username
# ***********************************************************************************************
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
            print(colored('The post has been downloaded!', "green"))
        else:
            print(colored('Post does not exist!', "red"))
    else:
        print(colored('Status code other than 200 received!', "red"))


# ***************************************************************************************
#          Get the list of recent media liked by the owner of id
# ****************************************************************************************
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
                print (colored(own_media['data'][0]['caption']['text'],'red'))
                print(colored("Image Name:", "blue")),
                print image_name
            else:
                print(colored("Image Name","blue")),
                print image_name
            print(colored('Your image has been downloaded!',"green"))
        else:
            print(colored('Post does not exist!',"red"))
    else:
        print(colored('Status code other than 200 received!','red'))

#  **********************************************************************************************
#             Function declaration to get the ID of the recent post of a user by username
# ************************************************************************************************
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
            print(colored('There is no recent post of the user!','red'))
    else:
        print(colored('Status code other than 200 received!','red'))


# *******************************************************************************************************
# The function below fetches all public post starting from the most recent one published by the user using 'GET'.
# **********************************************************************************************************
def get_user_post(username):
    user_id = get_user_id(username)  # get_user_id(username) function called here to get the user's ID
    user_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    request_user_recent_post = requests.get(user_url).json()  # GET call to fetch user's post
    return request_user_recent_post


# ***************************************************************************
#        The function below chooses the post in a creative way
# *************************************************************************
# Search the one which is most popular least popular and the recent one.
def search_post_by_choice(insta_username, option=0, post_selection=0, n=0):
    search_post = get_user_post(insta_username)      # This function is called here to get the user's post details.
    post_index = 0  # For most recent post
    like_on_a_post = []
    comment_on_a_post = []
    total_media = len(search_post['data'])             # To get the total no. of media
    if total_media == 0:
        print("This User has no footprints on instagram:-(!")
    else:
        if option == 1:  # For liking a post
            for each_media in range(0, total_media):
                like_on_a_post.append(search_post['data'][each_media]['likes']['count'])
            if post_selection == 1:  # If we want least popular post to be liked
                least_count = min(like_on_a_post)
                post_index = like_on_a_post.index(least_count)
            if post_selection == 2: # If we want recent post to be liked
                post_index = 0
            if post_selection == 3:  # If we want most popular post to be liked
                most_count = max(like_on_a_post)
                post_index = like_on_a_post.index(most_count)
            if post_selection == 4:
                post_index = n
        if option == 2 or 3 or 4 or 5 or 6:  # For commenting on a post
            for each_media in range(0, total_media):
                comment_on_a_post.append(search_post['data'][each_media]['comments']['count'])
            if post_selection == 1:  # If we want to commented on least popular post
                least_count = min(comment_on_a_post)
                post_index = comment_on_a_post.index(least_count)
            if post_selection == 2:  # If we want recent post to be commented
                post_index = 0
            if post_selection == 3:  # If we want to comment on most popular post
                most_count = max(comment_on_a_post)
                post_index = comment_on_a_post.index(most_count)
        print "Link to the Media        :", search_post['data'][post_index]['link']  # To print the link to a media.
        media_id = search_post["data"][post_index]['id']
        return media_id  # To return the particular media ID


# ************************************************************************************************************
#                      Function to get the list of comments on a post
# ****************************************************************************************************************
def get_list_of_comments(insta_username, option, post_selection):
    media_id = search_post_by_choice(insta_username, option, post_selection)
    request_url = BASE_URL + "media/" + media_id + "/comments?access_token=%s" %APP_ACCESS_TOKEN
    print 'GET request url : %s' % (request_url)
    comment_list = requests.get(request_url).json()
    if comment_list['meta']['code'] == 200:
        if len(comment_list['data']):
                for x in range(0,len(comment_list['data'])):
                    print(colored(comment_list['data'][x]['from']['username']+": ","red")),
                    print(colored(comment_list['data'][x]['text'],"blue"))
        else:
            print(colored("There was no comment found.","red"))
    else:
        print(colored("Status code other than 200 received.","red"))

# ************************************************************************************************************
#                      Function to get the list of likes on a post of choice
# ****************************************************************************************************************
def get_list_of_likes(insta_username, option, post_selection):
    media_id = search_post_by_choice(insta_username, option, post_selection)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    like_list = requests.get(request_url).json()
    if like_list['meta']['code'] == 200:
        if len(like_list['data']):
            for x in range(0, len(like_list['data'])):
                print(colored(like_list['data'][x]['username'], "red"))
        else:
            print(colored("There was no like found.", "red"))
    else:
        print(colored("Status code other than 200 received.", "red"))

# ************************************************************************************************************
# Function to like a users post by choice
# **************************************************************************************************************
def like_user_post(insta_username, option, post_selection, n):
    media_id = search_post_by_choice(insta_username, option, post_selection,n)
    like_post_url = BASE_URL + "media/" + media_id + "/likes"
    payload = {'access_token': APP_ACCESS_TOKEN}
    like = requests.post(like_post_url, payload).json()  # POST call to like the post
    if like['meta']['code'] == 200:
        print (colored('Bravo,Like was successful!',"green"))
    else:
        print(colored('Your like was unsuccessful. Try again!',"red"))

# ************************************************************************************
# Function to make a comment on a post of choice of the user
# **********************************************************************************
def post_a_comment(insta_username, option, post_selection):
    media_id = search_post_by_choice(insta_username, option, post_selection)
    url_post_comment = BASE_URL + "media/" + media_id + "/comments"
    input_comment = raw_input("Write a comment you want to post.\n")
    request_data = {"access_token": APP_ACCESS_TOKEN, 'text': input_comment}
    comment = requests.post(url_post_comment, request_data).json()  # POST call to comment the post
    if comment['meta']['code'] == 200:
        print (colored('Bravo.You successfully made a comment!',"green"))
    else:
        print(colored('Your comment was unsuccessful. Try again!',"red"))

# ***************************************************************************************
#  The Function gives Id of a comment that contains a particular word in a particular post
# ***************************************************************************************
def word_search_in_comment(insta_username,option,post_select):
    media_id = search_post_by_choice(insta_username, option, post_select)  # search_post_by_choice(username) function called here to get post ID
    url_post_comment = BASE_URL + "media/" + media_id + "/comments?access_token=" + APP_ACCESS_TOKEN
    all_comments = requests.get(url_post_comment).json()
    search_word = raw_input("Enter a word you want to search in the comments")
    print "\n<>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<>"
    comments_id = []
    list_of_comments = []
    user_name = []
    for each_comment in all_comments['data']:
        list_of_comments.append(each_comment['text'])
        comments_id.append(each_comment['id'])
        user_name.append(each_comment['from']['username'])
    comments_id_matched = []
    comments_matched = []
    user_found = []
    for each_item in range(len(list_of_comments)):  # Search for the comment that contains the specified word
        if search_word in list_of_comments[each_item]:
            comments_matched.append(list_of_comments[each_item])
            comments_id_matched.append(comments_id[each_item])
            user_found.append(user_name[each_item])
    if len(comments_matched) == 0:  # No comment Found with the word you searched
        print "No comment have word:" + search_word
        return False, media_id, False
    else:  # Comment found with word search!
        print "These comments contains the word:" + search_word
        for i in range(len(comments_matched)):
            print(colored(">>>>>>> " + comments_matched[i], "red"))
        return comments_id_matched, media_id, comments_matched


# ***************************************************************************
# Function declaration to make delete negative comments from the recent post
# ***************************************************************************
def delete_negative_comment(insta_username,option,post_select):
    media_id = search_post_by_choice(insta_username, option, post_select)
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
                    delete_url = (BASE_URL + 'media/%s/comments/%s?access_token=%s') % (
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

# **********************************************************
#        Plot most popular hashtags
# **********************************************************
def popular_hashtag():
    # ********************************* FOR FASHION HASHTAGS **************************************************
    tag_name1 = raw_input(
        colored("Choose from the category fashion<>repost,sports,fashion,pop,cultura,photography<>:- ", "blue"))
    request_url = (BASE_URL + 'tags/' + tag_name1 + '?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    popular_hash_tag = requests.get(request_url).json()
    if popular_hash_tag['meta']['code'] == 200:
        if len(popular_hash_tag['data']):
            media_count1 = popular_hash_tag["data"]["media_count"]
            print "MEDIA COUNT = " + str(media_count1)  # To Return the media count
        else:
            return None
    else:
        print 'Status code other than 200 received!'

    # ********************************************** FOR BLOGGER HASHTAGS ********************************************
    tag_name2 = raw_input(colored(
        "Choose from the category blogger<>happy,love ,blogger ,hairstyle ,tumblr ,tumblrgirl<>:- ",
        "magenta"))
    request_url = (BASE_URL + 'tags/' + tag_name2 + '?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    popular_hash_tag = requests.get(request_url).json()
    if popular_hash_tag['meta']['code'] == 200:
        if len(popular_hash_tag['data']):
            media_count2 = popular_hash_tag["data"]["media_count"]
            print "MEDIA COUNT=" + str(media_count2)  # To Return the media count
        else:
            return None
    else:
        print 'Status code other than 200 received!'

    # ******************************************* FOR FOOD HASHTAGS *****************************************
    tag_name3 = raw_input(
        colored("Choose from the category food<>foodlove ,chocolate, instafood, foodporn<>:- ", "green"))
    request_url = (BASE_URL + 'tags/' + tag_name3 + '?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    popular_hash_tag = requests.get(request_url).json()
    if popular_hash_tag['meta']['code'] == 200:
        if len(popular_hash_tag['data']):
            media_count3 = popular_hash_tag["data"]["media_count"]
            print"MEDIA COUNT =" + str(media_count3)  # To Return the media count
        else:
            return None
    else:
        print 'Status code other than 200 received!'

    # **************************************************** FOR TRAVEL HASHTAGS ******************************************
    tag_name4 = raw_input(colored(
        "Choose from the category travel<>travel ,instatravel ,travelgram ,tourism ,instago,travelblogger ,wanderlust<>:- ",
        "red"))
    request_url = (BASE_URL + 'tags/' + tag_name4 + '?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    popular_hash_tag = requests.get(request_url).json()
    if popular_hash_tag['meta']['code'] == 200:
        if len(popular_hash_tag['data']):
            media_count4 = popular_hash_tag["data"]["media_count"]
            print"MEDIA COUNT" + str(media_count4)  # To Return the media count
        else:
            return None
    else:
        print 'Status code other than 200 received!'
    print(colored("~~~~~~~~~~~~The pie-chart will be plotted on the basis of hashtags you chose for the categories~~~~~~~~~","red","on_cyan"))
    print(colored("<>~~~~~~~~~~~~~~~~~~~~~~~~The pie-chart is being plot with perfect counts~~~~~~~~~~~~~~~~~~~~~~~~~~~<>","red", "on_yellow"))
    print "~~~~~~@@~~~~~~~~@@@~~~~~~~~~~~~~@@@@@~~~~~~~~~~~~~~~~~~~~~~~@@@@@@@@@~~~~~~~~~~~~~~~~~~~~~~~~@@@@@@@@@@@@@@@"
    # Data to plot
    labels = 'Fahion'+"("+"#"+tag_name1+")", 'Blogger'+"("+"#"+tag_name2+")", 'Food'+"("+"#"+tag_name3+")", 'Travel'+"("+"#"+tag_name4+")"
    sizes = [media_count1, media_count2, media_count3, media_count4]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    return plt.show()


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
    print "Get a  particular user information"
    user_name = raw_input("Enter the name of username to display the info: rohittm or sarthaknegi3181 or frozenfire8888:- ")
    get_user_info(user_name)

    print"\n"
    choice = 'yes'
    while choice != 'no':
        print '\n'
        print "What would you like to do further?"
        print(colored("1:To Like a post of your choice of the user.", "magenta"))
        print(colored("2:To Comment on a post(not more than 200 words) of your choice of the user.", "magenta"))
        print(colored("3:To Search a word in the comment in the post of your choice of the user.", "magenta"))
        print(colored("4:To Get a list of comments on post of your choice of the user.","magenta"))
        print(colored("5:To Get a list of likes on post of your choice of the user.", "magenta"))
        print(colored("6:To Delete the negative comment from a post of your choice of the user.", "magenta"))
        print(colored("7:To Get your own recent post.", "magenta"))
        print(colored("8:To Get the recent post of a user by username.","magenta"))
        print(colored("9:To Get your recently liked media.","magenta"))
        print(colored("10:To determine images shared with a particular hash tag and plot using matplotlib.","magenta"))
        print "\n"
        option = int(raw_input("Your option: "))
        print "<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"
        if option not in range(1, 11):
            print"Invalid operation \nPlease try again!"
        elif option in range(1, 7):
            print "Which post you would wish to choose :"
            print "Press 1 for the one with the least popular."
            print "Press 2 for the one which has been uploaded recently. "
            print "Press 3 for the one which is the most popular."
            if option == 1:
                print "Press 4 to like all post"
            post_select = int(raw_input("Your option: "))
            if option == 1:
                user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi or frozenfire8888 :- ")
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
                    print" Sorry we have to perform the operation on the most recent post then"
            else:
                if post_select not in [1, 2, 3]:
                    print"Invalid post chosen \n"
            if option == 2:
                user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181 or frozenfire8888:- ")
                post_a_comment(user_name, option, post_select)
            if option == 3:
                user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181 or frozenfire8888:- ")
                word_search_in_comment(user_name, option, post_select)
            if option == 4:
                user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181 or frozenfire8888:- ")
                get_list_of_comments(user_name, option, post_select)
            if option == 5:
                user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181 or frozenfire8888:- ")
                get_list_of_likes(user_name, option, post_select)
            if option == 6:
                user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181 or frozenfire8888:- ")
                delete_negative_comment(user_name, option, post_select)
        if option == 7:
            user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181 or frozenfire8888:-")
            get_user_recent_post(user_name)
        if option == 8:
            user_name = raw_input("Enter the name of username to perform the function: rohittm or sarthaknegi3181 or frozenfire8888:-")
            get_user_recent_post(user_name)
        if option == 9:
            get_own_recently_liked()
        if option == 10:
            popular_hashtag()

        print "<>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<>"
        print "Do you want to continue?? (y/n)"
        opt = raw_input().upper()
        if opt == 'Y':
            choice = 'yes'
        elif opt == 'N':
            print "~~~~~~~~~~~~~~~Hope you had a good experience using instaBot~~~~~~~~~~~~~~~~~~~~~`"
            print "For any queries contact http://www.simranraj.com"
            print "<<<<<<<<<<<<<<<<<<<<<<<<<<Thank You have a nice day!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
            exit()
        else:
            print "Invalid choice"
            print "The program will shut down"
            print "@@@@@@@@@@@THANK YOU@@@@@@@@@@@@@@@"
            print "~~~~~~~~~~~~~~~Hope you had a good experience using instaBot~~~~~~~~~~~~~~~~~~~~~~~~"
            print "For any queries contact http://www.simranraj.com"
            print "<<<<<<<<<<<<<<<<<<<<<<<<Thank You have a nice day!>>>>>>>>>>>>>>>>>>>>>>>"
            exit()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FUNCTION END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
start_bot()