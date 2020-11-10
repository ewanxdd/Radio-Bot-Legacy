__all__ = (
    "NotGuildOwner",
    "is_guild_owner",
    "check",
    "is_owner",
    "bot_has_role",
    "bot_has_any_role",
    "bot_has_permissions",
    "guild_only",
    "is_nsfw",
    "cooldown",
    "has_any_role",
    "has_role",
    "has_permissions",
    "BucketType",
)

from discord.ext import commands as _commands
from discord.ext.commands import bot_has_role, guild_only, cooldown, has_any_role, has_role
from discord.ext.commands import check, is_owner, is_nsfw, bot_has_any_role, bot_has_permissions
from discord.ext.commands import has_permissions, BucketType


class NotGuildOwner(_commands.CheckFailure):
    """
    Raised if a command decorated with the ``@is_guild_owner()`` check is invoked by
    someone other than the guild owner.
    """

    def __init__(self):
        super().__init__("You are not the server owner, so you cannot run this command.")


def is_guild_owner():
    """
    A check returning true if the guild owner invoked the command, and we are in a guild.

    If we are not in a guild, we return False to fail the check. If we are not the guild
    owner, and one exists, we raise ``NotGuildOwner`` to show a custom error message.
    """

    def decorator(ctx):
        if not ctx.guild:
            return False
        elif not (ctx.guild.owner.id == ctx.author.id or ctx.author.id == ctx.bot.owner_id):
            raise NotGuildOwner
        return True

    return check(decorator)
