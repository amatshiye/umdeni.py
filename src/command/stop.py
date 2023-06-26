import discord

from src.handlers.command_handler import bot
from src.helpers.simple_embeds import simple_error_embed, simple_success_embed


@bot.command(name="stop")
async def stop_command(message: discord.Message):
    voice_client: discord.VoiceClient = bot.voice_clients[-1]

    if voice_client is None:
        print("Error:: Failed to find voice client.")
        await message.channel.send(embeds=[simple_error_embed("Not connected to voice.")])
        return

    if voice_client.is_playing():
        voice_client.stop()
        await message.channel.send(embeds=[simple_success_embed("Not connected to voice.")])
    else:
        await message.channel.send(embeds=[simple_error_embed("Current song not playing")])
        return

