import discord

from discord.ext import commands


class Requests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

    @commands.command()
    async def request(self, ctx, station, *, request: str):
        if station == "truckersfm" or station == "tfm":
            print("tfm code")
        if station == "simulatorradio" or station == "sr":
            print("sr code")



def setup(bot):
    bot.add_cog(Requests(bot))
