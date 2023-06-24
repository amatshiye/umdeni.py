import discord

from src.handlers.command_handler import bot
from src.helpers.simple_embeds import simple_success_embed, simple_error_embed


@bot.command(name="join")
async def join_command(message: discord.Message):
    channel = message.author.voice.channel

    if channel is not None:
        await channel.connect()
        await message.channel.send(embeds=[simple_success_embed(f"Joined **{channel.name}** channel.")])
    else:
        await message.channel.send(embeds=[simple_error_embed("Failed to join channel.")])
