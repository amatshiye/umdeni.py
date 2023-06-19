import json
import discord


class DiscordConfig:
    def __init__(self, token):
        self.token = token

    @staticmethod
    def from_json(json_data):
        return DiscordConfig(json_data['discord_token'])


def define_intents():
    intents = discord.Intents.default()
    intents.message_content = True

    return intents


def get_token():
    json_file = open("env.json")
    json_data = json.loads(json_file.read(), object_hook=DiscordConfig.from_json)
    return json_data.token
