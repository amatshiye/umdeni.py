import os.path
import subprocess
from asyncio import sleep
from typing import List

import discord

from core.song import Song
from src.helpers.simple_embeds import simple_success_embed


def download_song(link, voice_client: discord.VoiceClient):
    location = "player"
    file = "current.opus"

    delete_file(location, file, voice_client)
    subprocess.run(["yt-dlp", "--extract-audio", "--audio-format", "opus", "--audio-quality", "1", "-o",
                    f"{location}/{file}", link])


def delete_file(path_to_file, file, voice_client: discord.VoiceClient):
    if voice_client.is_playing() or voice_client.is_paused():
        return

    files = os.scandir(path_to_file)
    for _file in files:
        if _file.name == file:
            try:
                os.remove(_file)
            except PermissionError as error:
                print("Error:: Failed to delete file. Reason::", error)


async def pause_song(voice_client: discord.VoiceClient):
    if voice_client.is_playing():
        voice_client.pause()


async def resume_song(voice_client: discord.VoiceClient):
    if voice_client.is_paused():
        voice_client.resume()


class Player:
    def __init__(self, url, message: discord.Message):
        self.playlist_path = "./player/playlist.txt"
        self.current_song_path = "./player/current.opus"
        self.link = url
        self.songs: List[Song] = list()
        self.get_links_from_url()
        self.msg = message

    def get_links_from_url(self):
        if self.is_playlist():
            try:
                if os.path.exists(self.playlist_path):
                    os.remove(self.playlist_path)
                subprocess.run(["yt-dlp", f"{self.link}", "-j", "--flat-playlist", "--playlist-items", "1-5",
                                "--print-to-file", "%(url)s^&&^%(title)s^&&^%(duration)s", self.playlist_path])
                self.create_songs_list()
            except subprocess.CalledProcessError as error:
                print("Error:: Failed to get urls. Reason::", error)
                return
        else:
            self.add_new_song()
            print("Songs::", self.songs)

    def is_playlist(self):
        return not self.link.find("playlist") == -1

    def add_new_song(self):
        self.songs.append(self.link)

    def create_songs_list(self):
        with open(self.playlist_path, encoding="utf-8") as file:
            temp_songs = file.readlines()
            for temp_song in temp_songs:
                parts = temp_song.split("^&&^")

                duration = parts[2].replace("\n", "")
                if duration == "NA":
                    continue
                song = Song(url=parts[0], title=parts[1], duration=int(duration))
                self.songs.append(song)

    async def play_songs(self, voice_client: discord.VoiceClient):

        for song in self.songs:
            download_song(song.url, voice_client)
            try:
                await self.play_song(voice_client, song)
            except BaseException as error:
                print("Error:: Failed to play songs. Reason::", error)
                break

    async def play_song(self, voice_client: discord.VoiceClient, song: Song):
        if voice_client.is_paused() or voice_client.is_playing():
            return
        print("Playing url::", song.title)
        ffmpeg_options = {
            "options": f"-vn -ss 0"}

        audio_source = discord.FFmpegOpusAudio(source=self.current_song_path, **ffmpeg_options)
        try:
            voice_client.play(audio_source)
        except discord.errors.ClientException as error:
            print("Error:: Failed to play audio. Reason::", error)
            raise Exception(error)

        location = "player"
        file = "current.mp3"

        await self.msg.channel.send(embeds=[simple_success_embed(f"Now playing **{song.title}**")])
        while voice_client.is_playing() or voice_client.is_paused():
            await sleep(.1)

        if not voice_client.is_paused():
            delete_file(location, file, voice_client)
