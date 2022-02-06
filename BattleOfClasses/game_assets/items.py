class ItemBase:
    def __init__(self, name, price, weight):
        self._name = name
        self._price = price
        self._weight = weight

    def use(self):
        print(f"Using {self._name}")

    def __repr__(self):
        return f"{self._name} price: {self._price}"


class Weapon(ItemBase):
    def use(self):
        print(f"Slay the enemy with my {self._name}")


class Food(ItemBase):
    def use(self):
        print(f"Eating a piece of {self._name}")


class Drink(ItemBase):
    def use(self):
        print(f"Drinking a cup of {self._name}")


if __name__ == '__main__':
    sword = Weapon("Magic Sword", 200, 34)
    cheese = Food("Cheese", 10, 4)
    cup_of_beer = Drink("Beer", 10, 3)

    sword.use()
    cheese.use()
    cup_of_beer.use()