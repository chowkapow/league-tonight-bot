import discord
import json

from constants import game_format


def embed_team(team):
    id = team.get("id")
    game = team.get("game")
    time = team.get("time")
    players = team.get("players")
    embed = discord.Embed(title="Team {}".format(id), color=discord.Colour.dark_blue())
    i = 1
    result = ""
    for p in players:
        result += "{}. {}\n".format(i, p)
        i += 1
    embed.add_field(
        name="{}\nTime: {}".format(game_format.get(game), time),
        value=result,
        inline=False,
    )
    return embed


def lowercase_players(players):
    return [p.lower() for p in players]


def read_json(filename):
    with open(filename) as readfile:
        data = json.load(readfile)
        return data


def remove_player(players, player):
    for p in players:
        if p.lower() == player.lower():
            players.remove(p)
            return players


def write_json(data):
    with open("src/teams.json", "w") as outfile:
        json.dump(data, outfile, indent=2)
