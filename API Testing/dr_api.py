import requests


rq = requests.get("http://panel.discordradio.co/api/current")


artist = rq.json()["artist"]
title = rq.json()["title"]
art = rq.json()["art"]

print(artist)
print(title)
print(art)
