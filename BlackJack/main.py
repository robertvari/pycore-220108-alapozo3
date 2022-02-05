from game_assets.assets import Deck, Player, AIPlayer


class BlackJack:
    def __init__(self):
        self._intro()

        # create a deck of card
        self.deck = Deck()

        # todo create a player
        self.player = Player()

        # todo AI player
        # todo bet

    # protected method
    def _intro(self):
        print("="*50, "BlackJack Game", "="*50,)

BlackJack()