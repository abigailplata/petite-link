import requests
#cut.tly API documentation https://cutt.ly/api-documentation/cuttly-links-api

# replace your API key
api_key = "07f10e399fecb56b65f4c429f7f6b55d61d3c"

# the URL you'd like to shorten
url = input("Input Long URL:  ")

# preferred name in the URL

api_url = f"https://cutt.ly/api/api.php?key={api_key}&short=(url)"

# then make the requests
data = requests.get(api_url).json()["url"]

if data["status"] == 7:
	# OK, get short url
	shortened_url = data["shortlink"]
	print("Shortened URL:  ", shortened_url)
else:
	print("[!] Error Shortening URL:", data)
