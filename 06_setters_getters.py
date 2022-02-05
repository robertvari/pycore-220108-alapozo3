class Dice:
    def __init__(self, sides, color):
        self._sides = sides
        self._color = color
        self.__weight = 10

    # getter for sides
    def get_sides(self):
        return self._sides

    # getter for color
    def get_color(self):
        return self._color

    # getter for weight
    def get_weight(self):
        return f"The weight is: {self.__weight}"

    # setter for the color attribute
    def set_color(self, color):
        assert isinstance(color, str), "color must be of type string"
        self._color = color


my_dice = Dice(6, "white")
print(my_dice.get_sides())
print(my_dice.get_color())

my_dice.set_color("blue")
print(my_dice.get_color())

print(my_dice.get_weight())