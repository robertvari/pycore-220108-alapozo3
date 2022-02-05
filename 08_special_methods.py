class Dice:
    def __init__(self, color, sides):
        self._color = color
        self._sides = sides

    @property
    def sides(self):
        return self._sides

    @property
    def color(self):
        return self._color

    def __str__(self):
        return f"Color: {self._color} Sides: {self._sides}"


class Person:
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self._email = email

    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nEmail: {self._email}"

    def __repr__(self):
        return self._name


my_dice1 = Dice("White", 6)
my_dice2 = Dice("Red", 10)
my_dice3 = Dice("Blue", 20)
my_dices = [my_dice1,  my_dice2, my_dice3]

my_person1 = Person("Robert", 34, "robert@gmail.com")
my_person2 = Person("Csaba", 20, "csaba@gmail.com")
my_person3 = Person("Kriszta", 26, "kriszta@gmail.com")
my_persons = [my_person1, my_person2, my_person3]

print(my_dices)
print(my_persons)
print(my_person3)