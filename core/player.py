import os.path
import platform
import subprocess
from asyncio import sleep

import discord


def download_song(link):
    location = "player"
    file = "current.mp3"
    delete_song(location, file)

    subprocess.run(["yt-dlp", "--extract-audio", "--audio-format", "mp3", "-o", f"{location}/{file}", link])


def delete_song(path_to_file, file):
    path = os.path.join(path_to_file, file)
    os.remove(path)


async def pause_song(voice_client: discord.VoiceClient):
    voice_client.pause()


class Player:
    def __init__(self, url):
        self.playlist_path = "./player/playlist.txt"
        self.current_song_path = "./player/current.mp3"
        self.link = url
        self.songs = []
        self.get_links_from_url()

    def get_links_from_url(self):
        if self.is_playlist():
            try:
                subprocess.run(["yt-dlp", f"{self.link}", "-j", "--flat-playlist", "--print-to-file",
                                "url", self.playlist_path])
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
        with open(self.playlist_path) as file:
            temp_songs = file.readlines()
            for temp_song in temp_songs:
                self.songs.append(temp_song)
            print("Url List::", self.songs)

    async def play_songs(self, voice_client: discord.VoiceClient):

        for song in self.songs:
            download_song(song)
            await self.play_song(voice_client, song)

    async def play_song(self, voice_client: discord.VoiceClient, song):
        print("Playing url::", song)
        ffmpeg_options = {
            "options": f"-vn -ss 0"}

        audio_source = discord.FFmpegOpusAudio(source=self.current_song_path, **ffmpeg_options)
        voice_client.play(audio_source)

        location = "player"
        file = "current.mp3"

        while voice_client.is_playing():
            await sleep(.1)
        if not voice_client.is_playing() and not voice_client.is_paused():
            delete_song(location, file)
