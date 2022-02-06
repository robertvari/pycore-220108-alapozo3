import random, os

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

        # start first round
        self._start_round()

    def _start_round(self):
        self._clear_window()

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

        self._get_winner()

        if input("Do you want to play again? (y/n)") == "y":
            self._start_round()
        else:
            print("Have nice day!")
            exit()

    def _get_winner(self):
        player_list = [player for player in self._players if player.count_hand() <= 21]

        if player_list:
            winner_list = sorted(player_list, key=lambda player: player.count_hand())
            winner = winner_list[-1]

            print(f"The winner is: {winner.name} who wins: {self._bet}")
            winner.add_credits(self._bet)
        else:
            print("House wins!")

    def _clear_window(self):
        os.system("cls")

    # protected method
    def _intro(self):
        print("="*50, "BlackJack Game", "="*50,)

BlackJack()