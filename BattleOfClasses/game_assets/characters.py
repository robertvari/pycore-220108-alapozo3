import random
from game_assets.items import Weapon, Food, Drink


class CharacterBase:
    races = {
        "human": {"strength": 50, "max_HP": 100, "max_weight": 50},
        "ork": {"strength": 130, "max_HP": 200, "max_weight": 100},
        "elf": {"strength": 60, "max_HP": 100, "max_weight": 60},
        "dwarf": {"strength": 130, "max_HP": 230, "max_weight": 150},
    }

    def __init__(self):
        # base attributes
        self._name = None
        self._race = None
        self._golds = random.randint(0, 1000)

        # inventory
        self._inventory = []
        self._max_weight = 100
        self._right_hand = None
        self._left_hand = None

        # combat attributes
        self._strength = 0
        self._max_HP = 100
        self._current_HP = 0

    @staticmethod
    def get_fantasy_name():
        FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
                 'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
                 'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
                 'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
                 'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

        SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
                  'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
                  'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
                  'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
                  'wain', 'wan', 'win', 'wise', 'ya']

        return f"{random.choice(FIRST)}{random.choice(SECOND)}"

    def take_damage(self, damage):
        self._current_HP -= damage

    def attack(self, other):
        print(f"{self._name} attacks {other}")

        attack_strength = random.randint(0, self._strength)

        if attack_strength == 0:
            print(f"{self._name} misses {other}")
        else:
            print(f"{self._name} hits {other} with {attack_strength} strength")
            other.take_damage(attack_strength)

    @property
    def is_dead(self):
        return self._current_HP <= 0

    def _setup_attributes(self):
        self._strength = self.races[self._race]["strength"]
        self._max_HP = self.races[self._race]["max_HP"]
        self._current_HP = self._max_HP
        self._max_weight = self.races[self._race]["max_weight"]

    def show_character_card(self):
        print(f"Name: {self._name}")
        print(f"Race: {self._race}")
        print(f"Strength: {self._strength}")
        print(f"Max HP: {self._max_HP}")
        print(f"Max Weight: {self._max_weight}")
        print(f"Golds: {self._golds}")
        print(f"Left hand: {self._left_hand}")
        print(f"Right hand: {self._right_hand}")
        print(f"Inventory: {self._inventory}")

    @property
    def weapon_in_hand(self):
        return self._right_hand

    def __repr__(self):
        return f"{self._name}"


class Player(CharacterBase):
    def __init__(self):
        super().__init__()
        self._name = "Robert"
        #user_choice = input(f"What is your race? {list(self.races)}")

        self._race = "human"
        self._setup_attributes()


class NPC(CharacterBase):
    def __init__(self):
        super().__init__()
        self._name = self.get_fantasy_name()
        self._race = random.choice(list(self.races))
        self._setup_attributes()

        self._inventory += [
            Food("Cheese", 10, 3)
        ]

        self._right_hand = Weapon("Sword", 34, 7)


if __name__ == '__main__':
    npc = NPC()
    player = Player()