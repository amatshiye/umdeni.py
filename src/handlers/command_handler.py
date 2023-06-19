import discord

from src.command.disconnect import disconnect_command
from src.command.join import join_command

class CommandHandler:
    def __init__(self, message: discord.Message, context: discord.Client):
        self.cmd = None
        self.arg = None
        self.ctx = context
        self.msg = message

        self.parse_command()

    def parse_command(self):
        if len(self.msg.content) < 2:
            return
        if not self.msg.content.startswith("-") or self.msg.content.startswith(" ", 1):
            print("Error:: Command not found")
            return
        parts = self.msg.content.split("-")[1]
        args = parts.split(" ")
        if len(args) < 2:
            self.cmd = args[0]  # command
            return
        else:
            self.cmd = args[0]  # command
            self.arg = args[1]  # youtube link

    async def run_command(self):
        match self.cmd:
            case "join":
                await join_command(context=self.ctx, message=self.msg)
            case "dc":
                await disconnect_command(context=self.ctx, message=self.msg)
            case _:
                print("Error:: Command not found. Method::run_command")
