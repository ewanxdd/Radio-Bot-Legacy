import discord
import requests
import json

from discord.ext import commands

with open('config/config.json', 'r') as data:
    config = json.load(data)


class Station():
    def __init__(self,data):
        self.id = data["id"]

        self.name = data["info"]["name"]
        self.shortname = data["info"]["shortname"]
        self.emote = data["emote"]

        self.img_url = data["info"]["logo"]
        self.web_url = data["info"]["website"]

        self.slogan = data["info"]["slogan"]
        self.color = data["info"]["color"]

        self.stream_url = None
        if (data["stream"]["streamtype"] == "url"):
            self.stream_url = data["stream"]["streampath"]

        self.res_song_str = data["resolver"]["song"]
        self.res_dj_str = data["resolver"]["dj"]

    def getSong(self):
        return eval(self.res_song_str)
    def getDj(self):
        return eval(self.res_dj_str)

class Song():
    def __init__(self,name,artist,img):
        self.name = name
        self.artist = artist
        self.img = img

class Dj():
    def __init__(self,name,show,img,times):
        self.name = name
        self.show = show
        self.img = img
        self.startTime = times[0]
        self.endTime = times[1]

emojis = "🏠","<:BBCRADIO:618427383141367843>","<:global:618428539833810955>","<:bauer:618428924887826508>","🇫🇷","🇳🇱","🌐","✈","❌"

class Stations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s'])
    async def stations(self, ctx):

        def loadStations(file):
            f = open(file)
            read = f.read()
            f.close()
            data = json.loads(read)
            stations = {}
            for st in data:
                if (st["active"] == True):
                    stations[st["id"]] = Station(st)
            return stations

        def check_dir():
            try:
                os.mkdir("./stations")
            except Exception:
                pass


        check_dir()
        url = f"https://{config['stations_url']}/featured.json"
        r = requests.get(url)
        data = r.json()

        with open("./stations/featured.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        radioFile = "./stations/featured.json"
        vcs = {}
        gsts = {}
        stats = loadStations(radioFile)
        build = ""
        for sk in stats.keys():
            sv = stats[sk]

            build = build + f"{sv.emote} `{sv.id}` - {sv.name}\n"
            page = build

        featured = discord.Embed(title="Radio Bot Stations", description="Navigate through stations by country/ owner with the emotes below!")
        featured.add_field(name="Dont see your station?", value="Find an mp3 stream url to the station of your choice online and then do `/stream https://yourURL` If you need any assistance join our [Support Server](https://discord.gg/fpDHRE6)")
        featured.add_field(name="**Featured Stations!**", value="<:discord:644231688439988256>`discordradio` - Discord Radio", inline=False)
        msg = await ctx.send(embed=featured)
        await msg.add_reaction("<:BBCRADIO:618427383141367843>")
        await msg.add_reaction("<:global:618428539833810955>")
        await msg.add_reaction("<:bauer:618428924887826508>")
        await msg.add_reaction("🇫🇷")
        await msg.add_reaction("🇳🇱")
        await msg.add_reaction("🌐")
        await msg.add_reaction("✈")
        await msg.add_reaction("❌")


        def check(reaction, user):
            if str(reaction in [emojis]):
                if ctx.author == user:
                    return True
        while True:
            react, user = await self.bot.wait_for("reaction_add", check=check)






            #BBC

            if str(react) == "<:BBCRADIO:618427383141367843>":
                def check(reaction, user):
                    if str(reaction in emojis):
                        if ctx.author == user:
                            return True

                check_dir()
                url = f"https://{config['stations_url']}/bbc.json"
                r = requests.get(url)
                data = r.json()

                with open("./stations/bbc.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                radioFile = "./stations/bbc.json"
                vcs = {}
                gsts = {}
                stats = loadStations(radioFile)
                build = ""
                for sk in stats.keys():
                    sv = stats[sk]

                    build = build + f"{sv.emote} `{sv.id}` - {sv.name}\n"
                    page = build

                print("BBC Reacted")
                bbc = discord.Embed(title="Radio Stations Owned Operated by The BBC", description=page)
                await msg.edit(embed=bbc)
                await msg.remove_reaction("<:BBCRADIO:618427383141367843>", user)
                #react, user = await self.bot.wait_for("reaction_add", check=check)



            #GLOBAL

            if str(react) == "<:global:618428539833810955>":
                def check(reaction, user):
                    if str(reaction in emojis):
                        if ctx.author == user:
                            return True

                check_dir()
                url = f"https://{config['stations_url']}/global.json"
                r = requests.get(url)
                data = r.json()

                with open("./stations/global.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                radioFile = "./stations/global.json"
                vcs = {}
                gsts = {}
                stats = loadStations(radioFile)
                build = ""
                for sk in stats.keys():
                    sv = stats[sk]

                    build = build + f"{sv.emote} `{sv.id}` - {sv.name}\n"
                    page = build

                print("Global Reacted")
                #called glob as global is a func in python
                glob = discord.Embed(title="Radio Stations Operated by Global", description=page)
                await msg.edit(embed=glob)
                await msg.remove_reaction("<:global:618428539833810955>", user)
                #react, user = await self.bot.wait_for("reaction_add", check=check)





            #BAUER

            if str(react) == "<:bauer:618428924887826508>":
                def check(reaction, user):
                    if str(reaction in emojis):
                        if ctx.author == user:
                            return True

                print("Bauer Reacted")
                check_dir()
                url = f"https://{config['stations_url']}/bauer.json"
                r = requests.get(url)
                data = r.json()

                with open("./stations/bauer.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                radioFile = "./stations/bauer.json"
                vcs = {}
                gsts = {}
                stats = loadStations(radioFile)
                build = ""
                for sk in stats.keys():
                    sv = stats[sk]

                    build = build + f"{sv.emote} `{sv.id}` - {sv.name}\n"
                    page = build

                bauer = discord.Embed(title="Radio Stations Operated by Bauer Media Group", description=page)
                await msg.edit(embed=bauer)
                await msg.remove_reaction("<:bauer:618428924887826508>", user)
                #react, user = await self.bot.wait_for("reaction_add", check=check)




            #FRENCH STATIONS


            if str(react) == "🇫🇷":
                def check(reaction, user):
                    if str(reaction in emojis):
                        if ctx.author == user:
                            return True

                print("FR Reacted")
                check_dir()
                url = f"https://{config['stations_url']}/fr.json"
                r = requests.get(url)
                data = r.json()

                with open("./stations/fr.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                radioFile = "./stations/fr.json"
                vcs = {}
                gsts = {}
                stats = loadStations(radioFile)
                build = ""
                for sk in stats.keys():
                    sv = stats[sk]

                    build = build + f"{sv.emote} `{sv.id}` - {sv.name}\n"
                    page = build

                fr = discord.Embed(title="Radio Stations Broadcasting From France", description=page)
                await msg.edit(embed=fr)
                await msg.remove_reaction("🇫🇷", user)
                #react, user = await self.bot.wait_for("reaction_add", check=check)




            #DUTCH STATIONS

            if str(react) == "🇳🇱":
                def check(reaction, user):
                    if str(reaction in emojis):
                        if ctx.author == user:
                            return True

                print("NL Reacted")
                check_dir()
                url = f"https://{config['stations_url']}/nl.json"
                r = requests.get(url)
                data = r.json()

                with open("./stations/nl.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                radioFile = "./stations/nl.json"
                vcs = {}
                gsts = {}
                stats = loadStations(radioFile)
                build = ""
                for sk in stats.keys():
                    sv = stats[sk]

                    build = build + f"{sv.emote} `{sv.id}` - {sv.name}\n"
                    page = build

                bauer = discord.Embed(title="Radio Stations Broadcasting From Nederlands", description=page)
                await msg.edit(embed=bauer)
                await msg.remove_reaction("🇳🇱", user)
                #react, user = await self.bot.wait_for("reaction_add", check=check)

            if str(react) == "🌐":
                def check(reaction, user):
                    if str(reaction in emojis):
                        if ctx.author == user:
                            return True

                print("Online Reacted")
                check_dir()
                url = f"https://{config['stations_url']}/online.json"
                r = requests.get(url)
                data = r.json()

                with open("./stations/online.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                radioFile = "./stations/online.json"
                vcs = {}
                gsts = {}
                stats = loadStations(radioFile)
                build = ""
                for sk in stats.keys():
                    sv = stats[sk]

                    build = build + f"{sv.emote} `{sv.id}` - {sv.name}\n"
                    page = build

                bauer = discord.Embed(title="Radio Stations That Broadcast Online", description=page)
                await msg.edit(embed=bauer)
                await msg.remove_reaction("✈", user)
                #react, user = await self.bot.wait_for("reaction_add", check=check)


            if str(react) == "✈":
                def check(reaction, user):
                    if str(reaction in emojis):
                        if ctx.author == user:
                            return True

                print("ATC Reacted")
                check_dir()
                url = f"https://{config['stations_url']}/atc.json"
                r = requests.get(url)
                data = r.json()

                with open("./stations/atc.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                radioFile = "./stations/atc.json"
                vcs = {}
                gsts = {}
                stats = loadStations(radioFile)
                build = ""
                for sk in stats.keys():
                    sv = stats[sk]

                    build = build + f"{sv.emote} `{sv.id}` - {sv.name}\n"
                    page = build

                bauer = discord.Embed(title="Real Life Air Traffic Control", description=page)
                await msg.edit(embed=bauer)
                await msg.remove_reaction("✈", user)
                #react, user = await self.bot.wait_for("reaction_add", check=check)



            if str(react) == "❌":
                await msg.delete()
                await ctx.message.delete()



def setup(bot):
    bot.add_cog(Stations(bot))
