import unittest
import string
import random
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_game_is_word_valid(self):
        new_game = Game()
        new_game.grid = list("ABORIGENE")

        self.assertEqual(new_game.is_valid("ABORIGENE"), True)

    def test_game_is_word_invalid(self):
        new_game = Game()
        new_game.grid = list ("LOCALITES")

        self.assertEqual(new_game.is_valid("VILLAGES"), False)

    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
      self.assertIs(new_game.is_valid('FEUN'), False)
