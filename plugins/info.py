import socket
import platform
import discord


from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="Radio Bot Info", description="Information and statistics about Radio Bot")
        embed.add_field(name="Developer", value="<@210885581264125952>", inline=True)
        embed.add_field(name="Support Server", value="[Click Here](https://discord.gg/fpDHRE6)", inline=True)
        embed.add_field(name="Website", value="[radiobot.online](https://radiobot.online)", inline=True)
        embed.add_field(name="Shard Voice Connections", value=f"{len(self.bot.voice_clients)}", inline=True)
        embed.add_field(name="Shard ID", value=self.bot.shard_id, inline=True)
        embed.add_field(name="Shard Count", value=self.bot.shard_count, inline=True)
        embed.add_field(name="Shard Name", value=socket.gethostname(), inline=True)
        embed.add_field(name="Shard Platform", value=platform.system(), inline=True)
        embed.add_field(name="Platform Type", value=platform.release(), inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
