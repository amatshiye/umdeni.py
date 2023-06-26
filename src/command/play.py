import discord

from core.player import Player
from src.handlers.command_handler import bot
from src.helpers.simple_embeds import simple_success_embed, simple_error_embed


@bot.command(name="p")
async def p(message: discord.Message, link=None):
    await play_command(message, link)


@bot.command(name="play")
async def play(message: discord.Message, link=None):
    await play_command(message, link)


async def play_command(message: discord.Message, link=None):
    if link is None:
        await message.channel.send(embeds=[simple_error_embed("Please provide a link for this command.")])
        return
    voice_channel = message.author.guild.voice_client

    if voice_channel is None:
        channel = message.author.voice.channel
        await channel.connect()
    else:
        channel = voice_channel.channel

    # create player object
    bot.player = Player(url=link, message=message)

    await bot.player.play_songs(voice_client=bot.voice_clients[-1])
    await message.channel.send(embeds=[simple_success_embed(f"Currently in **{channel.name}** channel")])
