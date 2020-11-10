import discord

from checks.decs import *
from discord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    @commands.check(is_super)
    async def do_repeat(self, ctx, *, our_input: str):
        await ctx.send(our_input)

    @commands.command(aliases=["share"])
    async def screen(self, ctx):
        user = ctx.author
        uservoice = user.voice
        if uservoice == None or uservoice.channel == None:
            await ctx.send("You must be in a voice channel")
        else:
            await ctx.send(f"https://discordapp.com/channels/{ctx.guild.id}/{uservoice.channel.id}")

    @commands.command()
    async def shard(self, ctx):
        await ctx.send(self.bot.shard_id)


def setup(bot):
    bot.add_cog(Main(bot))
