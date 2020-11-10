import discord
import sys
import traceback
import json
import logger
import time
import requests

from flask import Flask
from flask import jsonify
from flask import request
from threading import Thread
from discord.ext import commands


with open('config/config.json', 'r') as data:
    config = json.load(data)

def get_prefix(bot, message):
    prefixes = config['prefix']
    return commands.when_mentioned_or(*prefixes)(bot, message)


plugins = [
    'plugins.main',
    'plugins.help',
    'events.on_dm',
    'events.on_shard_start',
    'events.on_guild_join',
    'events.on_guild_leave',
    'admin.dm',
    'plugins.s',
    'plugins.r',
    'admin.pull',
    'testing.decorator',
    'plugins.info'
]

if config["sharding"] == "True":
    bot = commands.Bot(command_prefix=get_prefix, shard_id=config["shard_id"], shard_count=config["shard_count"])
else:
    bot = commands.Bot(command_prefix=get_prefix)


#bot = commands.Bot(command_prefix="/", shard_id="1", shard_count="3")
bot.remove_command('help')
app = Flask(__name__)

if __name__ == '__main__':
    for plugin in plugins:
        try:
            bot.load_extension(plugin)
            logger.warn(f'{plugin} loaded')
        except Exception as e:
            logger.error(f'Failed to load extension {plugin}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():

    logger.info(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    activity = discord.Game(name="/help")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    logger.info(f'Successfully Started!')


def start():
    bot.run(config['token'], bot=True, reconnect=True)

start()
