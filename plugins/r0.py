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

import datetime as dt

from discord.ext import commands
from plugins import stats, vcs, gsts

def loadStreamFile(file):
    streams = []
    f = open(file,"r")
    read = f.read().lower().strip()
    f.close()
    reads = read.split("\n")
    #print(reads)
    filedata = {}
    if reads[0] != "[playlist]":
        print("INVAILD FILE")
    else:
        reads.pop(0)
        for i in reads:
            filedata[i.split("=",1)[0]] = i.split("=",1)[1]

        for i in range(int(filedata["numberofentries"])):
            streams.append(filedata["file{}".format(i+1)])

        #print("Found {} Streams in file '{}' ".format(len(streams),file))
        for s in streams:
            ac = "-"
            if (streams.index(s) == 0):
                ac = "*"
            #print("     {} {}".format(ac,s))

        return streams


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
        if (data["stream"]["streamtype"] == "file"):
            self.stream_url = loadStreamFile(data["stream"]["streampath"])[int(data["stream"]["streamid"])]

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

vcs = {}
gsts = {}

class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not after.channel and set(before.channel.members) == {member.guild.me}:
            if (member.guild.id in vcs.keys()):
                vcs[member.guild.id].stop()
                await vcs[member.guild.id].disconnect()
                try:
                    del vcs[member.guild.id]
                    del gsts[member.guild.id]
                    print("Removed ")
                except Exception:
                    pass

    @commands.command()
    async def rping(self, ctx):
        await ctx.send("Pong")


    @commands.command()
    @commands.guild_only()
    async def start(self, ctx, station):

        def loadStations(file):
            f = open(file)
            read = f.read()
            f.close()
            data = json.loads(read)
            stations = {}
            for st in data:
                if (st["active"] == True):
                    stations[st["id"]] = Station(st)
            return stations

        def check_dir():
            try:
                os.mkdir("./stations")
            except Exception:
                pass


        check_dir()
        url = "https://stations.radiobot.online/master.json"
        r = requests.get(url)
        data = r.json()

        with open("./stations/master.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        radioFile = "./stations/master.json"

        stats = loadStations(radioFile)


        if station == None:
            await ctx.send("You must specify a station")
        else:
            if station not in stats.keys():
                await ctx.send("That station does not exist")
            else:
                station2 = stats[station]
                user = ctx.author
                uservoice = user.voice
                if uservoice == None or uservoice.channel == None:
                    await ctx.send("You must be in a voice channel")
                else:
                    userchannel = uservoice.channel
                    vcs[ctx.guild.id] = await userchannel.connect()
                    asource = discord.FFmpegPCMAudio(station2.stream_url)
                    vcs[ctx.guild.id].play(asource)
                    await ctx.channel.send(f"Playing {station2.name}")

    @commands.command()
    @commands.guild_only()
    async def stream(self, ctx, stream:str):

        user = ctx.author
        uservoice = user.voice
        if uservoice == None or uservoice.channel == None:
            await ctx.send("You must be in a voice channel")
        else:
            userchannel = uservoice.channel
            vcs[ctx.guild.id] = await userchannel.connect()
            audio = discord.FFmpegPCMAudio(stream)
            vcs[ctx.guild.id].play(audio)
            await ctx.send(f"Playing {stream}")

    @commands.command()
    @commands.guild_only()
    async def stop(self, ctx):
        user = ctx.author
        uservoice = user.voice

        try:
            if ctx.guild.id in vcs.keys():
                vcs[ctx.guild.id].stop()
                await vcs[ctx.guild.id].disconnect()
                try:
                    del vcs[ctx.guild.id]
                    del gsts[ctx.guild.id]
                except Exception:
                    pass
                await ctx.send(":ok_hand:")
            else:
                await ctx.send("Nothing is playing")
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    @commands.guild_only()
    async def summon(self, ctx):
        user = ctx.author
        uservoice = user.voice
        if uservoice == None or uservoice.channel == None:
            await ctx.send("You must be in a voice channel")
        else:
            userchannel = uservoice.channel
            vcs[ctx.guild.id] = await userchannel.connect()

    @commands.command()
    @commands.guild_only()
    async def volume(self, ctx, volume:int):
        user = ctx.author
        uservoice = user.voice
        if uservoice == None or uservoice.channel == None:
            await ctx.send("I am not in a voice channel.")
        else:
            if not 0 < volume < 101:
                await ctx.send("Please enter a value between 1 and 100")
            else:
                state = self.voice_state.get(ctx.guild.id)
                player = state.player
                player.volume = volume
                await ctx.send(f"Volume set too {volume}")

    @commands.command()
    @commands.guild_only()
    async def station(self, ctx):
        await ctx.send("Meh, I will write this command another time :) ")


def setup(bot):
    bot.add_cog(Radio(bot))
