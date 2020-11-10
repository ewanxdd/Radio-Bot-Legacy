import json
import requests

url = "https://stations.radiobot.online/master.json"
resp = requests.get(url=url)
master = resp.json()


for i in master():
    print(i)
