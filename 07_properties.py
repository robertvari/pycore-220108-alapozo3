class Dice:
    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        assert isinstance(new_color, str), "color must be of type string"
        self.__color = new_color

    @property
    def sides(self):
        return self.__sides


my_dice = Dice("red", 6)
print(my_dice.color)
print(my_dice.sides)

my_dice.color = 10