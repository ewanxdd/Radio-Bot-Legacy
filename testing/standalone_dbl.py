import discord
import sys
import traceback
import json
#import logger
import time
import asyncio
import requests
import dbl

from flask import Flask
from flask import jsonify
from flask import request
from threading import Thread
from discord.ext import commands




bot = commands.Bot(command_prefix="??", shard_id=0, shard_count=4)





@bot.event
async def on_ready():

    token = '' # set this to your DBL token
    dblpy = dbl.DBLClient(bot, token)
    updating = bot.loop.create_task(update_stats())

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    activity = discord.Game(name="/help | radiobot.online")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'Successfully Started!')


    while True:
        print('Attempting to post server count')

        await dblpy.post_guild_count()
        print('Posted server count ({})'.format(dblpy.guild_count()))

        await asyncio.sleep(1800)



bot.run("", bot=True, reconnect=True)
