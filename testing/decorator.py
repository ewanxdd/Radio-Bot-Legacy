import discord
import json

from discord.ext import commands


with open('config/config.json', 'r') as data:
    config = json.load(data)

class Template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_super(ctx):
        for id in config["maintainers"]:
            if ctx.message.author.id == id:
                return True

    @commands.check(is_super)
    @commands.command()
    async def super(self, ctx):
        await ctx.send("Yes")


def setup(bot):
    bot.add_cog(Template(bot))
