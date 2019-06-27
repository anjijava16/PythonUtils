import requests
import urllib3

url = "https://api.twitter.com/1/statuses/user_timeline.json"
f1 = requests.get(url).json()
print(f1)
input = urllib3.get_host(url)
inputReq = urllib3.connection_from_url(url)
print(inputReq.ssl_version)
print(inputReq.headers)
print(input)
