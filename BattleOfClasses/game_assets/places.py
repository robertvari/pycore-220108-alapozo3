class PlaceBase:
    def __init__(self):
        self._name = None

    def enter(self, character):
        pass


class Tavern(PlaceBase):
    def enter(self, player):
        print(f"Welcome in the tavern {player}. I you have gold, you are in the right place.")


class Arena(PlaceBase):
    def enter(self, player):
        print(f"You are in the arena {player}. Fight for your life!")