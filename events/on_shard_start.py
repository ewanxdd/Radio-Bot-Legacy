import discord
import time
import logger
import json

import datetime as dt

from discord.ext import commands

with open('config/config.json', 'r') as data:
    config = json.load(data)


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        embed = discord.Embed(title=f"Shard {self.bot.shard_id} has came online!", description=f"Online serving {len(set(self.bot.get_all_members()))} users accross {len(self.bot.guilds)} servers", color = 0x00f742)
        embed.set_footer(text="You're seeing this as your are marked as a bot maintainer")
        embed.timestamp = dt.datetime.utcnow()

        ewan = await self.bot.fetch_user(210885581264125952)
        await ewan.send(embed=embed)

        arran = await self.bot.fetch_user(249919528421556224)
        await arran.send(embed=embed)

        #sam = await self.bot.fetch_user(190935064887033856)
        #await sam.send(embed=embed)



    @commands.command()
    async def shardstartevent(self, ctx):
        await ctx.send("shard Event Enabled")



def setup(bot):
    bot.add_cog(Ready(bot))
