import subprocess
from asyncio import sleep

import discord
import youtube_dl

from src.command.join import join_command


async def play_command(context: discord.Client, message: discord.Message):
    voice_client = None
    try:
        voice_client = await connect_to_channel(context, message)
    except Exception as error:
        voice_client = context.voice_clients[0]
        print("Error:: Failed to connect to channel. Reason::", error)

    url = "https://www.youtube.com/watch?v=Y3ZZw3gyxHk"

    subprocess.run(["rm", "-rf", "player/current.mp3"])
    subprocess.run(["yt-dlp", "--extract-audio", "--audio-format", "mp3", "-o", "player/current.mp3", url])

    ffmpeg_options = {
        "options": f"-vn -ss 0"}

    audio_source = discord.FFmpegOpusAudio(source="./player/current.mp3", **ffmpeg_options)
    voice_client.play(audio_source)
    
    while voice_client.is_playing():
        await sleep(.1)


async def connect_to_channel(context: discord.Client, message: discord.Message):
    return await join_command(context=context, message=message)
