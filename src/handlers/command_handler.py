from src.helpers.discord_config import define_intents
from discord.ext import commands

bot = commands.Bot(command_prefix="-", intents=define_intents())