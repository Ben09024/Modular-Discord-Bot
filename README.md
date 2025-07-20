# Modular Discord Bot

A minimal, modular Discord bot written in Python.  
Cogs (modules) are automatically detected and loaded at startup — no manual imports required.

##  Features

-  Auto-detects and loads all cogs from the `cogs/` directory
-  Clean modular structure for better scalability
-  Quick to deploy and easy to extend

Example Module:
```python
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello from MyCog!")

def setup(bot):
    bot.add_cog(MyCog(bot))



