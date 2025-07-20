import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            application_id=os.getenv('APPLICATION_ID')
        )

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f'{filename} wurde geladen.')

        await bot.tree.sync()

    async def on_ready(self):
        print(f'Bot ist eingeloggt als {self.user} (ID: {self.user.id})')
        print('------')

bot = MyBot()
bot.run(TOKEN)