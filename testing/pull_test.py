import requests
import json
import os

url = "https://stations.radiobot.online/master.json"
r = requests.get(url)
data = r.json()

try:
    os.mkdir("stations")
except Exception:
    pass

with open("stations/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
