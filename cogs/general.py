import discord
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('General Cog ist bereit.')

    @app_commands.command(name="hallo", description="Der Bot sagt Hallo!")
    async def hallo(self, interaction: discord.Interaction):
        """Sagt Hallo zum Benutzer."""
        await interaction.response.send_message(f'Hallo, {interaction.user.mention}!', ephemeral=True)

    @app_commands.command(name="ping", description="Zeigt die Latenz des Bots an.")
    async def ping(self, interaction: discord.Interaction):
        """Überprüft die Latenz des Bots."""
        latenz = round(self.bot.latency * 1000)
        await interaction.response.send_message(f'Pong! Die Latenz beträgt {latenz}ms.')

    @app_commands.command(name="serverinfo", description="Zeigt Informationen über den Server an.")
    async def serverinfo(self, interaction: discord.Interaction):
        """Gibt Details zum aktuellen Server aus."""
        server = interaction.guild
        embed = discord.Embed(
            title=f"Serverinformationen für {server.name}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=server.icon.url if server.icon else None)
        embed.add_field(name="Server ID", value=server.id, inline=True)
        embed.add_field(name="Besitzer", value=server.owner.mention, inline=True)
        embed.add_field(name="Mitgliederanzahl", value=server.member_count, inline=True)
        embed.add_field(name="Erstellt am", value=server.created_at.strftime("%d.%m.%Y"), inline=True)

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))