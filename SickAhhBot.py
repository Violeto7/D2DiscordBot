import discord
from discord.ext import commands
from datetime import date
import configparser

# Header files
import D2Featured

config=configparser.ConfigParser()
config.read('Config.ini')

MyBotKey = config['DiscordBotKey']['key']

D2Raids = D2Featured.D2Raids
D2Dungeons = D2Featured.D2Dungeons

class MyBot(commands.Bot):

    def __init__(self):
        intents=discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.load_extension("DailyJob")

client = MyBot()

@client.command(name='featured')
async def cmd_featured(ctx):
    D2Featured.updatePos()
    RaidPos1 = D2Featured.RaidPos1
    RaidPos2 = D2Featured.RaidPos2
    DungeonPos1 = D2Featured.DungeonPos1
    DungeonPos2 = D2Featured.DungeonPos2
    await ctx.send(f"The featured raids this week are:          **{D2Raids[RaidPos1]}** and **{D2Raids[RaidPos2]}**\nThe featured dungeons this week are:  **{D2Dungeons[DungeonPos1]}** and **{D2Dungeons[DungeonPos2]}**")


client.run(MyBotKey)