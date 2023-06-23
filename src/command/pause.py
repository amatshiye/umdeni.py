from core.player import Player


async def pause_command(player: Player):
    await player.pause_song()
