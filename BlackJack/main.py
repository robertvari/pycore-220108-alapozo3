from game_assets.assets import Deck, Player, AIPlayer


class BlackJack:
    def __init__(self):
        self._players = []

        self._intro()

        # create a deck of card
        self.deck = Deck()

        # create a player
        self.player = Player()
        self._players.append(self.player)

        # AI player
        self._players += [
            AIPlayer(),
            AIPlayer(),
            AIPlayer()
        ]

        print(self._players)

        # todo bet

    # protected method
    def _intro(self):
        print("="*50, "BlackJack Game", "="*50,)

BlackJack()