from typing import Any

import requests.exceptions
from discord import Intents

from src.handlers.command_handler import CommandHandler
from src.helpers.discord_config import get_token, define_intents
import discord


class Bot(discord.Client):
    def __init__(self, *, intents: Intents, **options: Any):
        super().__init__(intents=intents, **options)
        self.ch = None

    async def on_ready(self):
        print("Logged in as ", self.user.name)

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        if self.ch is None:
            self.ch = CommandHandler(message, self)

        try:
            if not self.ch.check_video_url():
                return
        except requests.exceptions.MissingSchema as error:
            await message.channel.send("Url is invalid.")
            print("Error:: Invalid url. Stacktrace::", error)
            return
        await self.ch.run_command()


if __name__ == "__main__":
    bot = Bot(intents=define_intents())
    bot.run(get_token())
