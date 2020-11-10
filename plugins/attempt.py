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

from discord.ext import commands

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


class Stations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def oldshite(self, ctx):
        radioFile = "./stations/master.json"
        vcs = {}
        gsts = {}
        stats = loadStations(radioFile)
        build = ""
        for sk in stats.keys():
            sv = stats[sk]
            build = build + "`{}` - {} {}\n".format(sv.id,sv.name,sv.emote)
            half = len(build)//2
            page_1 = "".join(build[:half])
            page_2 = "".join(build[half:])

        e_page_1 = discord.Embed()
        e_page_1.add_field(name = "Page 1:", value=page_1)
        e_page_1.set_footer(text="Dont see your station? Contact Ewan#9902 to get it added!")
        await ctx.send(embed=e_page_1)

        e_page_2 = discord.Embed()
        e_page_2.add_field(name = "Page 2:", value=page_2)
        e_page_2.set_footer(text="Dont see your station? Contact Ewan#9902 to get it added!")
        await ctx.channel.send(embed=e_page_2)

    @commands.command()
    async def stations(self, ctx):
        uk1 = discord.Embed(title="UK Stations :flag_gb:", description="Some text here idk what.")
        uk1.add_field(name="Station 1", value="`stationname`", inline=False)
        uk1.add_field(name="Station 2", value="`station2name`", inline=False)

        msg = await ctx.send(embed=uk1)
        await msg.add_reaction("🇬🇧")
        await msg.add_reaction("🇺🇸")
        await msg.add_reaction("❌")

        def check(reaction, user):
            if str(reaction in ["🇬🇧","🇺🇸","❌"]):
                if ctx.author == user:
                    return True

        react, user = await self.bot.wait_for("reaction_add", check=check)

        if str(react) == "🇬🇧":
            def check(reaction, user):
                if str(reaction in ["🇬🇧","🇺🇸","❌"]):
                    if ctx.author == user:
                        return True

            print("GB Reacted")
            uk1 = discord.Embed(title="UK Stations :flag_gb:", description="Some text here idk what.")
            uk1.add_field(name="Station 1", value="`stationname`", inline=False)
            uk1.add_field(name="Station 2", value="`station2name`", inline=False)
            await msg.edit(embed=uk1)
            await msg.remove_reaction("🇬🇧", user)
            react, user = await self.bot.wait_for("reaction_add", check=check)
        if str(react) == "🇺🇸":
            def check(reaction, user):
                if str(reaction in ["🇬🇧","🇺🇸","❌"]):
                    if ctx.author == user:
                        return True
            print("US Reacted")
            us1 = discord.Embed(title="US Stations :flag_us:", description="Some text here idk what.")
            us1.add_field(name="Station 1", value="`stationname`", inline=False)
            us1.add_field(name="Station 2", value="`station2name`", inline=False)
            await msg.edit(embed=us1)
            await msg.remove_reaction("🇺🇸", user)
            react, user = await self.bot.wait_for("reaction_add", check=check)
        if str(react) == "❌":
            await msg.delete()
            await ctx.message.delete()



def setup(bot):
    bot.add_cog(Stations(bot))
