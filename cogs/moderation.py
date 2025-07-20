import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation Cog ist bereit.')

    @app_commands.command(name="clear", description="Löscht eine bestimmte Anzahl von Nachrichten.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, anzahl: int):
        """Löscht Nachrichten in einem Kanal."""
        if anzahl <= 0:
            await interaction.response.send_message("Bitte gib eine positive Zahl an.", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)
        geloescht = await interaction.channel.purge(limit=anzahl)
        await interaction.followup.send(f'{len(geloescht)} Nachrichten wurden gelöscht.', ephemeral=True)

    @clear.error
    async def clear_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message("Du hast nicht die erforderlichen Berechtigungen, um diesen Befehl zu verwenden.", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))