import json

from discord.ext import commands as _commands


with open('config/config.json', 'r') as data:
    config = json.load(data)

'''
def check_maintainer(ctx):
    return maintainer in config["maintainers"]

async def check_super(ctx):
    for super_admin in config["super_admin"]:
        admin = await self.bot.fetch_user(super_admin)
        return admin


is_maintainer = commands.check(check_maintainer)
is_super = commands.check(check_super)
'''


class NotMaintainer(_commands.CheckFailure):
    def __init__(self):
        super().__init__("You are not a maintainer")

def is_maintainer():
    def decorator(ctx):
        for maintainer in config["maintainers"]:
            if not maintainer:
                raise NotMaintainer
    return check(decorator)
