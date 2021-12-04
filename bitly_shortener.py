### Link shortener using Bitly API and request python libraries
### reference: https://www.thepythoncode.com/article/make-url-shortener-in-python

import requests

#account information:
username = "o_24br6eq2n7" 
password = "Opportunity23!" ##replace password from original Bitly account

url = input("Input Long URL:  ")

#get access token:
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))

# used requests.post() method to make a POST request to /oauth/access_token 
# endpoint and get our access token. We passed auth parameter to add our account credentials to the request headers.

if auth_res.status_code == 200:
	#if response is good, get the access token
	access_token = auth_res.content.decode()
	print("[!] Got access token:", access_token)
else: 
	print("[!] Cannot get access token, exiting...")
	exit()
	
# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account before shortening URL
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers) #downloaded API from Bitly
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()

# make the POST request to get shortened URL for `url`
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200:
    # if response is OK, get the shortened URL
    link = shorten_res.json().get("link")
    print("Petite URL:", link)
