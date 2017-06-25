# instaBot
 A bot which follows your commands for Instagram.

````````````````````````
Name:Instabot-4
Version:1.0
Description:A terminal bot app using python that allows you to use the various features of the Instagram API and also deals with data science by determining number of images shared with a particular hash tag and plotting it using "matplotlib".
Author Name:Simran Raj
Author Url:http://www.simranraj.com
``````````````````````````

 
 # Objectives:
* To Like a post of your choice of the user.
* To Comment on a post(not more than 200 words) of your choice of the user.
* To Search a word in the comment in the post of your choice of the user.
* To Get a list of comments on post of your choice of the user.
* To Get a list of likes on post of your choice of the user.
* To Delete the negative comment from a post of your choice of the user.
* To Get your own recent post.
* To Get the recent post of a user by username.
* To Get your recently liked media.
* To determine images shared with a particular hash tag and plot using matplotlib.

 

# Generate your own APP_ACCESS_TOKEN

```````````````````````````````````````
1.Goto https://instagram.com/developer
2.Click on Manage Clients tab in the header.
3.If not already logged in, login in using your existing instagram account.
4.Click on Register a new client, the green colored button just below the header on the right.
5.Fill out the form with the valid url in the Valid redirect URIs field.
6.Click on register.
7.Uncheck the “Disable implicit OAuth” under under the security tab.
8.Copy the client-id.
9.HIT (Replace client Id,redirect-url and response-token)
https://api.instagram.com/oauth/authorize/?
client_id=CLIENT-ID
&redirect_uri=REDIRECT-URI
&response_type=token
&scope=basic+public_content+likes+comments
10.You will be redirected to:
http://your-redirect-uri/#access_token=ACCESS-TOKEN
11.Copy the ACCESS-TOKEN at a safe place.

````````````````````````````````````````````
### Python setup

To properly use this python-modules some additional libraries have to be
installed beforehand. This can be easily accomplished with the commands below.

```bash
pip install virtual_env
source bin/activate
pip install requests
pip install termcolor
pip install urlib
pip install matplotlib
pip install TextBlob
```

### Run 
To run the app type the command given below.

```bash
python instaBot.py
```
