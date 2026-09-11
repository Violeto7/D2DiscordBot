import discord
from discord.ext import commands
from datetime import date
import configparser
import os

# Header files
import D2Featured

config=configparser.ConfigParser()

# Get the absolute path of the folder where this script lives
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.ini')

config.read(config_path)

MyBotKey = config['discordbotkey']['key']

D2Raids = D2Featured.D2Raids
D2Dungeons = D2Featured.D2Dungeons

class MyBot(commands.Bot):

    def __init__(self):
        intents=discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents, help_command=None) # help_command=None so we can override the default help command with our own

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

@client.command(name='help')
async def cmd_help(ctx):
    await ctx.send(
f"""
### **The currently implemented commands are as follows:**
> - !help     - Display all currently implemented commands along with a brief description (dude, you just did this surely we don't need this)
> - !featured - Lists the featured raids and dungeons for this week
""")


client.run(MyBotKey)