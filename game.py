import string
import random

class Game:
    def __init__(self):
        self.grid = []
        for _ in range (9):
            self.grid.append(random.choice(string.ascii_letters).upper())

    def is_word_valid(self, word):

        grid_copy = self.grid[:]

        for letter in word:
            if letter not in grid_copy:
                return False
            else:
                grid_copy.remove(letter)

        return True
