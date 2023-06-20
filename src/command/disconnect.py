import discord


async def disconnect_command(context: discord.Client, message: discord.Message):
    await context.voice_clients[0].disconnect(force=False)
