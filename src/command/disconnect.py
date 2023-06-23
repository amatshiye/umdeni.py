import discord
from discord.ext import commands

from src.handlers.command_handler import bot
from src.handlers.simple_embeds import simple_error_embed


@bot.command("dc")
async def dc(message: discord.Message):
    await disconnect_command(message)


@bot.command("leave")
async def leave(message: discord.Message):
    await disconnect_command(message)


async def disconnect_command(message: discord.Message):
    voice_client = message.guild.voice_client

    if voice_client is not None:
        await voice_client.disconnect()
    else:
        print("Error:: Failed to disconnect. Reason:: Bot not in a voice channel")
        await message.channel.send(embeds=[simple_error_embed("Not in a voice channel")])
