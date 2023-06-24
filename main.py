
from discord.ext import commands

from src.handlers.bot_commands import bot_commands
from src.helpers.discord_config import get_token
from src.handlers.command_handler import bot

if __name__ == "__main__":
    try:
        bot.run(token=get_token())
        bot.all_commands.clear()
        bot_commands()
    except commands.errors.MissingRequiredArgument as error:
        print(error)
