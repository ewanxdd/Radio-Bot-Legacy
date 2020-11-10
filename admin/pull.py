import discord
import requests
import json
import os

from discord.ext import commands

from checks.decs import *


class Pull(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def pull2(self, ctx, update:str):
        try:
            os.mkdir("stations")
        except Exception:
            pass
        if update == "master":

            url = "https://stations.radiobot.online/master.json"
            r = requests.get(url)
            data = r.json()


            with open("./stations/master.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                await ctx.send("Updated Master")
        elif update == "bbc":
            check_dir()
            url = "https://stations.radiobot.online/bbc.json"
            r = requests.get(url)
            data = r.json()

            with open("./stations/uk1.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                await ctx.send("Updated Master")
        elif update == "global":
            check_dir()
            url = "https://stations.radiobot.online/global.json"
            r = requests.get(url)
            data = r.json()

            with open("./stations/global.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                await ctx.send("Updated Global")
        elif update == "bauer":
            check_dir()
            url = "https://stations.radiobot.online/bauer.json"
            r = requests.get(url)
            data = r.json()

            with open("./stations/bauer.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                await ctx.send("Updated Bauer")
        elif update == "nl":
            check_dir()
            url = "https://stations.radiobot.online/nl.json"
            r = requests.get(url)
            data = r.json()

            with open("./stations/nl.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                await ctx.send("Updated NL")

            with open("/stations/data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)




def setup(bot):
    bot.add_cog(Pull(bot))
