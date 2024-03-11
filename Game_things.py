class Thing:
    def __init__(self, type):
        self.type = type


class Armor(Thing):
    def __init__(self):
        super().__init__("Броня")
        self.level = 1


class Weapon(Thing):
    def __init__(self):
        super().__init__("Оружие")
        self.level = 1


class Eat(Thing):
    def __init__(self, name, points, type, permanent):
        super().__init__("Еда")
        self.name = name
        self.points = points
        self.type = type
        self.permanent = permanent


TYPE_HP = 0
TYPE_ATTACK = 1
FOOD = [
    Eat("Авакадо", 50, TYPE_HP, False),
    Eat("Груша", 25, TYPE_ATTACK, False),
    Eat("Яблоко", 3, TYPE_HP, True),
    Eat("Банан", 2, TYPE_ATTACK, True),
]
