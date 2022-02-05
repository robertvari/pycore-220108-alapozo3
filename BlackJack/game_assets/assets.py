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



class Player:
    def __init__(self):
        self._hande = []


# testing my assets
if __name__ == '__main__':
    deck = Deck()
    print(deck.cards)
    print(len(deck.cards))