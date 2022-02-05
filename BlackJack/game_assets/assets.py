class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def __repr__(self):
        return f"{self._name} {self._value}"


class Deck:
    def __init__(self):
        self._cards = []

    @property
    def cards(self):
        return self._cards

class Player:
    def __init__(self):
        self._hande = []


# testing my assets
if __name__ == '__main__':
    deck = Deck()
    print(deck.cards)