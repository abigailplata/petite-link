### Link shortener using Bitly API and request python libraries
###
#reference: https://www.thepythoncode.com/article/make-url-shortener-in-python

import requests

#account credentials
username = "o_24br6eq2n7"
password = "O7212k13"

#get the access token
auth_res = request.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))

if auth_res.status_code == 200;
	#if response is good, get the access token
	access_token = auth_res.content.decode()
	print("[!] Got access token:", access_token)
else: 
	print("[!] Cannot get access token, exiting...")
	exit()