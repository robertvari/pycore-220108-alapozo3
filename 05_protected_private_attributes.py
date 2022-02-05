class Dice:
    def __init__(self):
        self.color = "red"
        self.sides = 6

        # protected attribute
        self._weight = 10

        # private attribute
        self.__my_birthday = "__my_birthday"

        print(self.__my_birthday)


my_dice = Dice()
print(my_dice.color)
print(my_dice.sides)
my_dice.color = "blue"

print(my_dice._weight)
my_dice._weight = "Hello"
print(my_dice._weight)

# print(my_dice.__my_birthday)