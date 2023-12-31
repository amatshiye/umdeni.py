import discord

from core.player import pause_song
from src.handlers.command_handler import bot
from src.helpers.simple_embeds import simple_error_embed, simple_success_embed


@bot.command(name="pause")
async def pause_command(message: discord.Message):
    voice_client: discord.VoiceClient = bot.voice_clients[-1]
    if voice_client is None:
        await message.channel.send(embeds=[simple_error_embed("Not connected to voice.")])
        return

    if voice_client.is_playing():
        await pause_song(voice_client)
        await message.channel.send(embeds=[simple_success_embed("Paused.")])
    else:
        await message.channel.send(embeds=[simple_error_embed("Current song not playing.")])

