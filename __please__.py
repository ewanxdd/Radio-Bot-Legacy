import discord
import requests
import subprocess
import datetime
import os
import sys
import time
import socket
import platform
import psutil
import json


OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus():
    for opus_lib in OPUS_LIBS:
        try:
            discord.opus.load_opus(opus_lib)
            return
        except OSError:
            pass

load_opus()

url = "https://stations.radiobot.online/master.json"
resp = requests.get(url=url)
master = resp.json()


class Station():
    def __init__(self,data):
        data_i = int(data["id"])
        self.id = data_i

        self.name = data["info"]["name"]
        self.shortname = data["info"]["shortname"]
        self.emote = data["emote"]

        self.img_url = data["info"]["logo"]
        self.web_url = data["info"]["website"]

        self.slogan = data["info"]["slogan"]
        self.color = data["info"]["color"]

        self.stream_url = None

        self.res_song_str = data["resolver"]["song"]
        self.res_dj_str = data["resolver"]["dj"]

    def getSong(self):
        return eval(self.res_song_str)
    def getDj(self):
        return eval(self.res_dj_str)

class Song():
    def __init__(self,name,artist,img):
        self.name = name
        self.artist = artist
        self.img = img

class Dj():
    def __init__(self,name,show,img,times):
        self.name = name
        self.show = show
        self.img = img
        self.startTime = times[0]
        self.endTime = times[1]

<<<<<<< HEAD:testing/init test.py
def loadStations(url):
    return master
=======
def loadStations(file):
    return master

>>>>>>> 73540e171b586781b1c4d80438cefd32abc074cb:__please__.py


vcs = {}
gsts = {}
stats = loadStations(master)

<<<<<<< HEAD:testing/init test.py
print(stats[])
=======
what_station = input("Enter a station: ")
for i in stats.name():
    json_raw = raw.readlines()
    json_object = json.loads(json.loads[i])
    if what_station not in stats():
        print("That station does not exist")
    else:
        print(station)
>>>>>>> 73540e171b586781b1c4d80438cefd32abc074cb:__please__.py
