import discord

from src.handlers.command_handler import bot
from src.helpers.simple_embeds import simple_error_embed, simple_success_embed


@bot.command("dc")
async def dc(message: discord.Message):
    await disconnect_command(message)


@bot.command("leave")
async def leave(message: discord.Message):
    await disconnect_command(message)


async def disconnect_command(message: discord.Message):
    voice_client = message.guild.voice_client

    if voice_client is not None:
        await voice_client.disconnect(force=True)
        await message.channel.send(embeds=[simple_success_embed("Disconnected.")])
    else:
        print("Error:: Failed to disconnect. Reason:: Bot not in a voice channel")
        await message.channel.send(embeds=[simple_error_embed("Not in a voice channel")])
