import discord


async def join_command(context: discord.Client, message: discord.Message):
    return await message.author.voice.channel.connect(self_deaf=True)
