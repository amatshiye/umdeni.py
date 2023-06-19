import discord


async def join_command(context: discord.Client, message: discord.Message):
    await message.author.voice.channel.connect()
