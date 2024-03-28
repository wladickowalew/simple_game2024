from random import randint


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
    def __init__(self, name, points, type, permanent, rarity):
        super().__init__("Еда")
        self.name = name
        self.points = points
        self.type = type
        self.permanent = permanent
        self.rarity = rarity

    def __str__(self):
        return f"EAT ({self.name}, {self.type}, {self.rarity})"


class Eat_Builder:
    TYPE_HP = 0
    TYPE_ATTACK = 1
    FOOD = [
        Eat("Авакадо", 50, TYPE_HP, False, 10),  # 1 - 10
        Eat("Груша", 25, TYPE_ATTACK, False, 10),  # 11 - 20
        Eat("Яблоко", 3, TYPE_HP, True, 1),  # 21 - 21
        Eat("Банан", 2, TYPE_ATTACK, True, 1)  # 22 - 22
    ]

    def create_rarity_intervals(self):
        sp = []
        t = 1
        for item in self.FOOD:
            t2 = t + item.rarity - 1
            sp.append((t, t2))
            t = t2 + 1
        return sp

    def __init__(self):
        self.rarity_intervals = self.create_rarity_intervals()
        self.max_rarity = self.rarity_intervals[-1][-1]

    def get_food(self):
        num = randint(1, self.max_rarity)
        for i in range(len(self.rarity_intervals)):
            a, b = self.rarity_intervals[i]
            if a <= num <= b:
                return self.FOOD[i]
