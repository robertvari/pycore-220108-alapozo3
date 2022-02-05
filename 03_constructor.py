class Dice:
    # constructor of a class
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color


my_dice1 = Dice(6, "white")
my_dice2 = Dice(10, "blue")
my_dice3 = Dice(20, "red")

print(my_dice1.sides, my_dice1.color)
print(my_dice2.sides, my_dice2.color)
print(my_dice3.sides, my_dice3.color)