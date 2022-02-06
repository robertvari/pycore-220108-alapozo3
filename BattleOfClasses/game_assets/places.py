from game_assets.characters import NPC


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
        enemy = NPC()
        print(f"You are in the arena {self._main_game.player}. {enemy} is running towards you with a {enemy.weapon_in_hand}.")

        while True:
            enemy.attack(self._main_game.player)

            if self._main_game.player.is_dead:
                print(f"{self._main_game.player} is dead :(((")
                break

            self._main_game.player.attack(enemy)

            if enemy.is_dead:
                print(f"{enemy} is dead")
                break

# Tavern IS PlaceBase?
# PlaceBase HAS BattleOfClasse