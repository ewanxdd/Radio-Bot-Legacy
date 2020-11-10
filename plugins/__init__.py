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

with open('config/config.json', 'r') as data:
    config = json.load(data)

radioFile = "./stations/master.json"
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus():
    for opus_lib in OPUS_LIBS:
        try:
            discord.opus.load_opus(opus_lib)
            return
        except OSError:
            pass

load_opus()


url = f"https://{config['stations_url']}/master.json"
resp = requests.get(url=url)
master = resp.json()


class Station():
    def __init__(self,data):
        self.id = data["id"]

        self.name = data["info"]["name"]
        self.shortname = data["info"]["shortname"]
        self.emote = data["emote"]

        self.img_url = data["info"]["logo"]
        self.web_url = data["info"]["website"]

        self.slogan = data["info"]["slogan"]
        self.color = data["info"]["color"]

        self.stream_url = None
        if (data["stream"]["streamtype"] == "url"):
            self.stream_url = data["stream"]["streampath"]
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


global vcs
global gsts

vcs = {}
gsts = {}

def loadStations(file):
    data = master
    stations = {}
    for st in data:
        if (st["active"] == True):
            stations[st["id"]] = Station(st)
    return stations



vcs = {}
gsts = {}
stats = loadStations(master)

#print(stats)
