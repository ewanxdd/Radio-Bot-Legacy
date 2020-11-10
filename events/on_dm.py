import discord
import time
import logger
import json

import datetime as dt

from discord.ext import commands

with open('config/config.json', 'r') as data:
    config = json.load(data)


class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild == None:
            if message.author.id != self.bot.user.id:
                #print(message)
                if message.content.startswith(config["prefix"]):
                    return
                msg = message.content
                embed = discord.Embed(
                    title = f"{message.author} - {message.author.id}",
                    description = f"{msg}",
                    color = 0xb300ff
                )
                embed.set_footer(text="You are seeing this as you are a bot maintainer")
                embed.timestamp = dt.datetime.utcnow()

                ewan = await self.bot.fetch_user(210885581264125952)
                await ewan.send(embed=embed)

                arran = await self.bot.fetch_user(249919528421556224)
                await arran.send(embed=embed)

                sam = await self.bot.fetch_user(190935064887033856)
                await sam.send(embed=embed)



    @commands.command()
    async def dmevent(self, ctx):
        await ctx.send("DM Event Enabled")



def setup(bot):
    bot.add_cog(Dm(bot))
