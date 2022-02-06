class PlaceBase:
    def __init__(self, main_game):
        self._name = None
        self._main_game = main_game

    def enter(self):
        pass


class Tavern(PlaceBase):
    def enter(self):
        self._main_game.clear_screen()
        print(f"Welcome in the tavern {self._main_game.player}. I you have gold, you are in the right place.")


class Arena(PlaceBase):
    def enter(self):
        self._main_game.clear_screen()
        print(f"You are in the arena {self._main_game.player}. Fight for your life!")

# Tavern IS PlaceBase?
# PlaceBase HAS BattleOfClasse