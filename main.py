from src.handlers.command_handler import CommandHandler
from src.helpers.discord_config import get_token, define_intents
import discord


class Bot(discord.Client):
    async def on_ready(self):
        print("Logged in as ", self.user.name)

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        ch = CommandHandler(message, self)
        await ch.run_command()


if __name__ == "__main__":
    bot = Bot(intents=define_intents())
    bot.run(get_token())
