import random


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

    def __repr__(self):
        return f"{self._name}"


class Player(CharacterBase):
    def __init__(self):
        super().__init__()
        self._name = input("What is your name?")


class NPC(CharacterBase):
    def __init__(self):
        super().__init__()
        self._name = self.get_fantasy_name()


if __name__ == '__main__':
    npc = NPC()
    enemy = NPC()
    player = Player()
    print(npc)
    print(enemy)
    print(player)