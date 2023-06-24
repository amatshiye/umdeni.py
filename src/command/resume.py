import discord

from src.handlers.command_handler import bot
from src.helpers.simple_embeds import simple_error_embed, simple_success_embed


@bot.command(name="resume")
async def resume_command(message: discord.Message):
    voice_client: discord.VoiceClient = bot.voice_clients[-1]
    if voice_client is None:
        await message.channel.send(embeds=[simple_error_embed("Not connected to voice.")])
        return

    if voice_client.is_paused():
        voice_client.resume()
        await message.channel.send(embeds=[simple_success_embed("Resumed.")])
    else:
        await message.channel.send(embeds=[simple_error_embed("Current song not paused.")])