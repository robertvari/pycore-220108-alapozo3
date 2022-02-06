class CharacterBase:
    def __init__(self):
        # base attributes
        self._name = None
        self._race = None
        self._golds = 0

        # inventory
        self._inventory = []
        self._max_weight = 100
        self._right_hand = None
        self._left_hand = None

        # combat attributes
        self._strength = 0
        self._max_HP = 100
        self._current_HP = 0