from src.helpers.discord_config import get_token, define_intents
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-", intents=define_intents())
