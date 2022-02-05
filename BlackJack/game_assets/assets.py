class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def __repr__(self):
        return f"{self._name} {self._value}"


class Deck:
    pass


class Player:
    def __init__(self):
        self._hande = []


# testing my assets
if __name__ == '__main__':
    card1 = Card("Club Ace", 11)
    card2 = Card("Club 3", 3)
    card3 = Card("Spade 7", 7)

    hande = [card1, card2, card3]
    print(hande)