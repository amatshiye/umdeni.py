import string

import discord
import requests as requests

from core.player import Player
from src.command.disconnect import disconnect_command
from src.command.join import join_command
from src.command.play import play_command


class CommandHandler:
    def __init__(self, message: discord.Message, context: discord.Client):
        self.cmd = None
        self.arg = None
        self.player = None
        self.ctx = context
        self.msg = message

        self.parse_command()

    def parse_command(self):
        if len(self.msg.content) < 2:
            return
        if not self.msg.content.startswith("-") or self.msg.content.startswith(" ", 1):
            print("Error:: Command not found")
            return
        parts = self.msg.content.split("-", maxsplit=1)[1]
        args = parts.split(" ")
        if len(args) < 2:
            self.cmd = args[0]  # command
            return
        else:
            self.cmd = args[0]  # command
            self.arg = args[1]  # youtube link

    def check_video_url(self):
        if self.arg is None:
            return False
        if not self.arg.find("youtu"):
            print("Error:: Not a valid youtube link")
            return False

        request = requests.get(self.arg)
        return request.status_code == 200

    async def run_command(self):
        match self.cmd:
            case "join":
                await join_command(context=self.ctx, message=self.msg)
            case "dc":
                await disconnect_command(context=self.ctx, message=self.msg)
            case "p":
                self.player = Player(self.arg)
                await play_command(context=self.ctx, message=self.msg, player=self.player)
            case _:
                print("Error:: Command not found. Method::run_command")
