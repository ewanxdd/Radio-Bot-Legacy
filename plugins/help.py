import discord
import json

from checks.decs import *
from discord.ext import commands

with open('config/config.json', 'r') as data:
    config = json.load(data)

global prefix
prefix = config['prefix']
version = config['version']
support_invite = config["support_invite"]

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        helpembed = discord.Embed(
            title=f"Radio Bot {version}",
            description="Commands for the Radio Bot "
            )
        helpembed.add_field(
            name=prefix+"ping",
            value="Check that the bot is online & working",
            inline=False
            )
        helpembed.add_field(
            name=prefix+"info",
            value="Nerdy stats about Radio Bot",
            inline=False
        )
        helpembed.add_field(
            name=prefix+"stations",
            value="View the list of all stations.",
            inline=False
        )
        helpembed.add_field(
            name=prefix+"start `station`",
            value="Start a Radio Station of your choice.",
            inline=False
        )
        helpembed.add_field(
            name=prefix+"stream",
            value="Start a radio stream of your choice.",
            inline=False
        )
        helpembed.add_field(
            name=prefix+"station",
            value="Shows what station is playing."
        )
        helpembed.set_footer(text="This is a fresh release of the Radio Bot rewrite, you may find that some commands have not yet been added.")
        await ctx.send(":mailbox_with_mail:")
        await ctx.message.author.send(embed=helpembed)
        await ctx.message.author.send(support_invite)


    @commands.command()
    @commands.check(is_super)
    async def ahelp(self, ctx):
        ahelpembed = discord.Embed(
            title="Radio Mod",
            description="Commands for the Radio Bot rewrite"
            )
        ahelpembed.add_field(
            name=prefix+"ping",
            value="Check that the bot is online & working",
            inline=False
            )
        await ctx.send(":mailbox_with_mail:")
        await ctx.author.send(embed=ahelpembed)




def setup(bot):
    bot.add_cog(Help(bot))
