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


my_dice1 = Dice("White", 6)
my_dice2 = Dice("Red", 10)

my_person = Person("Robert", 34, "robert@gmail.com")
print(my_person)