# instaBot
 A bot which follows your commands for Instagram.
 

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
