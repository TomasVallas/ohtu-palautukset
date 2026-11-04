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
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_loytaa_pelaajan(self):
        pelaaja = self.stats.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")

    def test_search_palauttaa_none_jos_ei_loydy(self):
        self.assertIsNone(self.stats.search("Selanne"))

    def test_team_palauttaa_joukkueen_pelaajat(self):
        nimet = [p.name for p in self.stats.team("EDM")]
        self.assertEqual(nimet, ["Semenko", "Kurri", "Gretzky"])

    def test_top_palauttaa_parhaat_jarjestyksessa(self):
        nimet = [p.name for p in self.stats.top(2)]
        self.assertEqual(nimet[0], "Gretzky")
        self.assertEqual(nimet[1], "Lemieux")
