class Dice:
    sides = 6
    color = "white"


my_dice1 = Dice()

my_dice2 = Dice()
my_dice2.color = "blue"
my_dice2.sides = 10

my_dice3 = Dice()
my_dice3.color = "red"
my_dice3.sides = 20

print(my_dice1.color, my_dice1.sides)
print(my_dice2.color, my_dice2.sides)
print(my_dice3.color, my_dice3.sides)