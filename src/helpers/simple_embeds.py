import discord


def simple_success_embed(message: str):
    return discord.Embed(color=discord.Color.green(), description=message)


def simple_error_embed(message: str):
    return discord.Embed(color=discord.Color.red(), description=message)
