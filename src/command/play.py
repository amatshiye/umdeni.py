
import discord

from core.player import Player
from src.command.join import join_command


async def play_command(context: discord.Client, message: discord.Message, player: Player):
    voice_client = None
    try:
        voice_client = await connect_to_channel(context, message)
    except Exception as error:
        voice_client = context.voice_clients[0]
        print("Error:: Failed to connect to channel. Reason::", error)

    await player.play_songs(voice_client)


async def connect_to_channel(context: discord.Client, message: discord.Message):
    return await join_command(context=context, message=message)
