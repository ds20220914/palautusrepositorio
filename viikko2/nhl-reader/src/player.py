import requests


class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict["team"]
        self.nationality = dict["nationality"]
        self.games = dict["games"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]
    def __str__(self):
        goals_assists = self.goals + self.assists
        return f"{self.name:20} {self.team:4}  {self.goals:2}+{self.assists:2}={goals_assists:3}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(player_data) for player_data in response]

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self.reader.get_players()
        finnish_players = filter(lambda player: player.nationality == nationality, players)
        sorted_players = sorted(finnish_players, key=lambda p: p.goals + p.assists, reverse=True)

        return sorted_players
