import discord


class CommandHandler:
    def __init__(self, message: discord.Message, context: discord.Client):
        self.cmd = None
        self.arg = None
        self.ctx = context
        self.msg = message

        self.parse_command()
        self.run_command()

    def parse_command(self):
        if len(self.msg.content) < 2:
            return
        if not self.msg.content.startswith("-") or self.msg.content.startswith(" ", 1):
            print("Error:: Command not found")
            return
        parts = self.msg.content.split("-")[1]
        args = parts.split(" ")
        if len(args) < 1:
            return
        self.cmd = args[0]  # command
        self.arg = args[1]  # youtube link

    def run_command(self):
        print("Command:", self.cmd)
        print("Link:", self.arg)
