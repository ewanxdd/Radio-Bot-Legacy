__all__ = ("Permissions",)

import enum
import typing

import discord


class Permissions(enum.IntFlag):
    NONE = 0x00000000
    CREATE_INSTANT_INVITE = 0x00000001
    KICK_MEMBERS = 0x00000002
    BAN_MEMBERS = 0x00000004
    ADMINISTRATOR = 0x00000008
    MANAGE_CHANNELS = 0x00000010
    MANAGE_GUILD = 0x00000020
    ADD_REACTIONS = 0x00000040
    VIEW_AUDIT_LOG = 0x00000080
    READ_MESSAGES = 0x00000400
    SEND_MESSAGES = 0x00000800
    SEND_TTS_MESSAGES = 0x00001000
    MANAGE_MESSAGES = 0x00002000
    EMBED_LINKS = 0x00004000
    ATTACH_FILES = 0x00008000
    READ_MESSAGE_HISTORY = 0x00010000
    MENTION_EVERYONE = 0x00020000
    USE_EXTERNAL_EMOJIS = 0x00040000
    CONNECT = 0x00100000
    SPEAK = 0x00200000
    MUTE_MEMBERS = 0x00400000
    DEAFEN_MEMBERS = 0x00800000
    MOVE_MEMBERS = 0x01000000
    USE_VAD = 0x02000000
    CHANGE_NICKNAME = 0x04000000
    MANAGE_NICKNAMES = 0x08000000
    MANAGE_ROLES = 0x10000000
    MANAGE_WEBHOOKS = 0x20000000
    MANAGE_EMOJIS = 0x40000000

    def __new__(cls, value):
        if isinstance(value, discord.Permissions):
            value = value.value
        return super().__new__(cls, value)

    def __iter__(self):
        for name, value in type(self).__members__.items():
            if value & self:
                yield name, bool(value)

    def _iter_bitwise(self):
        for name, value in type(self).__members__.items():
            yield name, value

    def unmask(self) -> typing.List[typing.Tuple[str, int]]:
        """
        Takes a masked set of permissions and returns each set bit as a string
        of the corresponding permission names in a list.
        """
        return [p for p in self._iter_bitwise()]


    @classmethod
    def none(cls):
        """A factory method that creates a :class:`Permissions` with all
        permissions set to False."""
        return cls(0b00000000000000000000000000000000)

    @classmethod
    def all(cls):
        """A factory method that creates a :class:`Permissions` with all
        permissions set to True."""
        return cls(0b01111111111101111111110011111111)

    @classmethod
    def all_channel(cls):
        """A :class:`Permissions` with all channel-specific permissions set to
        True and the guild-specific ones set to False. The guild-specific
        permissions are currently:

        - manage_guild
        - kick_members
        - ban_members
        - administrator
        - change_nicknames
        - manage_nicknames
        """
        return cls(0b00110011111101111111110001010001)

    @classmethod
    def general(cls):
        """A factory method that creates a :class:`Permissions` with all
        "General" permissions from the official Discord UI set to True."""
        return cls(0b01111100000000000000000010111111)

    @classmethod
    def text(cls):
        """A factory method that creates a :class:`Permissions` with all
        "Text" permissions from the official Discord UI set to True."""
        return cls(0b00000000000001111111110001000000)

    @classmethod
    def voice(cls):
        """A factory method that creates a :class:`Permissions` with all
        "Voice" permissions from the official Discord UI set to True."""
        return cls(0b00000011111100000000000000000000)
