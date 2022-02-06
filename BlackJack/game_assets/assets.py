import random


class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def name(self):
        return self._name

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

        while self._in_game:
            # count hand
            hand_value = self._count_hand()

            if hand_value > 16:
                self._in_game = False

                if hand_value > 21:
                    print(f"{self._name} lost this round")
                else:
                    print(f"{self._name} passes")
            else:
                new_card = deck.draw()

                # if new_card is an ace
                if "Ace" in new_card.name and hand_value > 10:
                    new_card.value = 1
                self._hand.append(new_card)

    def reset(self):
        self._hand.clear()
        self._in_game = True

    def _count_hand(self):
        return sum([card.value for card in self._hand])

    def __str__(self):
        return f"Name: {self._name}\nCredits: {self._credits}\nHand: {self._hand}\nHand value: {self._count_hand()}"


class Player(PlayerBase):
    def __init__(self):
        super(Player, self).__init__()

        self._name = input("what is your name?")

    def draw_card(self, deck: Deck):
        # todo start hand

        print(f"Cards is your hand: {self._hand}")
        print(f"Your hand value: {self._count_hand()}")

        response = input("Do you want to draw a card? (y/n)")
        while response == "y":
            new_card = deck.draw()
            print(f"The new card: {new_card}")

            self._hand.append(new_card)

            print(f"Cards is your hand: {self._hand}")
            print(f"Your hand value: {self._count_hand()}")

            if self._count_hand() > 21:
                print("You lost this round :(")
                break

            response = input("Do you want to draw a card? (y/n)")

        self._in_game = False


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

    player = Player()
    player.draw_card(deck)
    print(player)
