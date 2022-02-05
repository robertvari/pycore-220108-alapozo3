from game_assets.assets import Deck, Player


class BlackJack:
    def __init__(self):
        self._intro()

        # todo create a deck of card
        self.deck = Deck()

        # todo create a player
        self.player = Player()

        # todo AI player
        # todo bet

    # protected method
    def _intro(self):
        print("="*50, "BlackJack Game", "="*50,)

BlackJack()