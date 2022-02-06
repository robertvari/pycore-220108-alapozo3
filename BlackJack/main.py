import random

from game_assets.assets import Deck, Player, AIPlayer


class BlackJack:
    def __init__(self):
        self._players = []
        self._bet = 0
        self._min_bet = 10

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

        self._start_round()

    def _start_round(self):
        # shuffle player list
        random.shuffle(self._players)

        # create a new deck
        self.deck.create()

        # reset all players
        [player.reset() for player in self._players]

        self._bet = 0
        for player in self._players:
            # give bet
            self._bet += player.give_bet(self._min_bet)

            # setup starting hand
            player.set_start_hand(self.deck)

        for player in self._players:
            player.draw_card(self.deck)


    # protected method
    def _intro(self):
        print("="*50, "BlackJack Game", "="*50,)

BlackJack()