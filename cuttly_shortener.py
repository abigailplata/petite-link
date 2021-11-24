import requests

# replace your API key
api_key = ""

# the URL you'd like to shorten
url = ""

# preferred name in the URL

api_url = f"https://cutt.ly/api/api.php?key={api_key}&short=(url)"

# then make the requests
data = requests.get(api_url).json()["url"]

if data["status"] == 7:
	# OK, get short url
	petite_url = data["petitelink"]
	print(Petite URL:", petite_url)
else:
	print("[!] Error Shortening URL:", data)

