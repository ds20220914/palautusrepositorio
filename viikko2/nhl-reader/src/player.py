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

