import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # Annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub.get_players)

    def test_search_existing_player(self):
        player = self.stats.search("Yzerman")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Yzerman")
        self.assertEqual(player.team, "DET")
        self.assertEqual(player.goals, 42)
        self.assertEqual(player.assists, 56)

    def test_search_non_existing_player(self):
        player = self.stats.search("NonExistingPlayer")
        self.assertIsNone(player)

    def test_team_existing(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_team_non_existing(self):
        players = self.stats.team("NHL")
        self.assertEqual(len(players), 0)

    def test_top(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)






