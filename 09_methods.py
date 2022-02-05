import random


class Dice:
    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides
        self.__current_side = 1

    @property
    def color(self):
        return self.__color

    @property
    def sides(self):
        return self.__sides

    @property
    def current_side(self):
        return self.__current_side

    def roll(self):
        self.__current_side = random.randint(1, self.__sides)

    def __str__(self):
        return f"Color: {self.__color} Sides: {self.__sides}"


my_dice1 = Dice("White", 6)
my_dice1.roll()

my_dice2 = Dice("Blue", 10)
my_dice2.roll()

print(my_dice1, my_dice1.current_side)
print(my_dice2, my_dice2.current_side)