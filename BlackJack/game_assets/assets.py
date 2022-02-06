import random


class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def __repr__(self):
        return f"{self._name} {self._value}"


class Deck:
    def __init__(self):
        self._cards = []
        self.create()

    @property
    def cards(self):
        return self._cards

    def create(self):
        self._cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card in cards:
                card_name = f"{name} {card[0]}"
                card_value = card[1]

                self._cards.append(
                    Card(card_name, card_value)
                )

        random.shuffle(self._cards)

    def draw(self):
        new_card = self._cards[0]
        self._cards.remove(new_card)
        return new_card


class PlayerBase:
    first_names = ["Brittney", "Curtis", "Lucas", "Chip", "Simon"]
    last_names = ["Moriah", "Tristin", "Troy", "Gale", "Lynn"]

    def __init__(self):
        self._name = None
        self._hand = []
        self._credits = random.randint(10, 100)
        self._in_game = True

    def draw_card(self, deck: Deck):
        new_card = deck.draw()
        self._hand.append(new_card)

    def __str__(self):
        return f"Name: {self._name}\nCredits: {self._credits}\nHand: {self._hand}"


class Player(PlayerBase):
    pass


class AIPlayer(PlayerBase):
    # method override
    def __init__(self):
        # base class __init__ call
        super().__init__()

        # do your own stuff
        self._name = f"{random.choice(self.first_names)} {random.choice(self.last_names)}"


# testing my assets
if __name__ == '__main__':
    deck = Deck()

    ai_player1 = AIPlayer()
    ai_player1.draw_card(deck)
    print(ai_player1)
