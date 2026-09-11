import datetime
from discord.ext import tasks, commands
from zoneinfo import ZoneInfo
from datetime import date

# Header files
import D2Featured

D2Raids = D2Featured.D2Raids
D2Dungeons = D2Featured.D2Dungeons

TARGET_ZONE = ZoneInfo("America/New_York")
# Replace with the exact time you want to test (e.g., 5 minutes from right now)
TASK_TIME = datetime.time(hour=10, minute=0, tzinfo=TARGET_ZONE) 

class DailyJobCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.daily_task.start()

    def cog_unload(self):
        self.daily_task.cancel()

    @tasks.loop(time=TASK_TIME)
    async def daily_task(self):
        D2Featured.updatePos()
        RaidPos1 = D2Featured.RaidPos1
        RaidPos2 = D2Featured.RaidPos2
        DungeonPos1 = D2Featured.DungeonPos1
        DungeonPos2 = D2Featured.DungeonPos2
        # 1. Check the time right when the task triggers
        print("Executing daily task right now!")
        if datetime.datetime.now(TARGET_ZONE).strftime("%A") != "Tuesday":
            print("Skipping because it isn't Tuesday and Featured Raids and Dungeons have not changed")
            return

        channel_id = 1527755212960301286  # Double check your channel ID
        role_id = 1547422582867759105
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(f"<&{role_id}>\nThe featured raids this week are:          **{D2Raids[RaidPos1]}** and **{D2Raids[RaidPos2]}**\nThe featured dungeons this week are:  **{D2Dungeons[DungeonPos1]}** and **{D2Dungeons[DungeonPos2]}**")

        # 2. Log when the NEXT day's execution will happen
        # Now that the loop has run once, this will NOT be None
        print(f"Task successfully processed. Next scheduled run: {self.daily_task.next_iteration}")

    @daily_task.before_loop
    async def before_daily_task(self):
        # Wait until the bot is completely connected to Discord
        await self.bot.wait_until_ready()
        print("Daily task loop has been initialized and is waiting for the target time.")

async def setup(bot: commands.Bot):
    await bot.add_cog(DailyJobCog(bot))