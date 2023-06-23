import discord

from src.handlers.command_handler import bot
from src.handlers.simple_embeds import simple_success_embed


@bot.command(name="ping")
async def ping(message: discord.Message):
    await message.channel.send(embeds=[simple_success_embed("Pong!")])


