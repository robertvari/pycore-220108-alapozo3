import os
from game_assets.characters import Player
from game_assets.places import Arena, Tavern


class BattleOfClasses:
    def __init__(self):
        self.clear_screen()
        self.intro()

        self._player = Player()

        # places
        self._tavern = Tavern(self)
        self._arena = Arena(self)

        self._arena.enter()

    @property
    def player(self):
        return self._player

    def intro(self):
        print("-"*50, "BATTLE OF CLASSES", "-"*50)

    @staticmethod
    def clear_screen():
        print("clear_screen called")
        os.system("cls")


BattleOfClasses()