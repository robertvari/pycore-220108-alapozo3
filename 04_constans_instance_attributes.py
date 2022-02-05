class Dice:
    # class attributes
    dices_created = 0

    def __init__(self, color, sides):
        # instance attribute
        self.color = color
        self.sides = sides
        Dice.dices_created += 1


my_dice1 = Dice("white", 6)
my_dice2 = Dice("white", 6)
my_dice3 = Dice("white", 6)
my_dice4 = Dice("white", 6)

print(my_dice1.dices_created)
print(my_dice4.dices_created)