from typing import Any

import requests.exceptions
from discord import Intents

from src.command.disconnect import dc, leave
from src.command.join import join_command
from src.command.ping import ping
from src.handlers.command_handler import bot
from src.helpers.discord_config import get_token


def commands():
    bot.add_command(ping)
    bot.add_command(join_command)
    bot.add_command(dc)
    bot.add_command(leave)


@bot.command(name="test")
async def test(etx, arg):
    print("Testing commands approach!:", arg)


bot.run(token=get_token())
commands()
