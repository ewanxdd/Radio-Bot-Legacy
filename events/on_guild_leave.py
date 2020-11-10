import discord
import time
import logger
import json

import datetime as dt

from discord.ext import commands

with open('config/config.json', 'r') as data:
    config = json.load(data)


class OnLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        embed = discord.Embed(title=f"I have been removed from a server!", description=f"I have been removed from {guild.owner}'s server {guild.name} <{guild.id}> it had {len(guild.members)} members", color = 0xb03f45)
        embed.add_field(name=f"I am now in {len(self.bot.guilds)} servers", value="\u200b")
        embed.set_footer(text="You're seeing this as your are marked as a bot maintainer")
        embed.timestamp = dt.datetime.utcnow()

        ewan = await self.bot.fetch_user(210885581264125952)
        await ewan.send(embed=embed)

        arran = await self.bot.fetch_user(249919528421556224)
        await arran.send(embed=embed)

        #sam = await self.bot.fetch_user(190935064887033856)
        #await sam.send(embed=embed)



    @commands.command()
    async def onleavevent(self, ctx):
        await ctx.send("shard Event Enabled")



def setup(bot):
    bot.add_cog(OnLeave(bot))
