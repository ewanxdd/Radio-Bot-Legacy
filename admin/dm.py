import discord
from decorators import *

import datetime as dt

from discord.ext import commands

class Dm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def dm(self, ctx, id, *, args:str):
        message = args
        user = await self.bot.fetch_user(id)
        embed = discord.Embed(title = f"Message from Radio Bot Maintainer {ctx.author}", description=message)
        embed.set_footer(text="To reply to this message, send your message in this DM")
        embed.timestamp = dt.datetime.utcnow()
        try:
            await user.send(embed=embed)
            await ctx.send(":thumbsup:")
        except Exception as e:
            await ctx.send("I can't send a message to this user, they probably have me blocked.")

def setup(bot):
    bot.add_cog(Dm(bot))
