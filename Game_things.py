from random import randint, choice, random


class Thing:
    def __init__(self, type, mass):
        self.type = type
        self.mass = mass


class Armor(Thing):
    ARMOR_PROBABILITY = 33
    NAMES = [
        "Плотная кольчужная броня", "Лордовская пластинчатая доспеха", "Рыцарский латный доспех",
        "Герцогская масонская броня", "Крестьянская кожаная доспеха", "Барональная стальная кольчуга",
        "Дружинная железная бригантина", "Шайкская шкура мантия", "Монашеский роба",
        "Ординский плащ-накидка", "Викингская кольчужная рубаха", "Телеранская цельная плита",
        "Элфийский дружищща лучник", "Гномий каменный щит", "Гоблинская шапка с шлемом",
        "Жрический заклинательный плащ", "Орковский берсеркерский кожаный доспех", "Троллья кожаная кираса",
        "Эльфийский небесный пластинчатым доспех", "Гномий огненный щит"
    ]

    def __init__(self, level=1):
        super().__init__("Броня", randint(50, 100) / 10)
        self.name = choice(self.NAMES)
        self.level = 1 if level < 1 else level

    def __str__(self):
        return f"ARMOR ({self.name}, {self.level}, {self.mass}))"



class Weapon(Thing):
    WEAPON_PROBABILITY = 33
    NAMES = [
        "Драконий клинок", "Лунный молот", "Кровавый пик", "Грозовой посох",
        "Пламенный меч", "Тенистый кинжал", "Каменный буран", "Вихревая булава",
        "Роскошный рапир", "Смертоносный топор", "Пепельный арбалет", "Солнечная палица",
        "Могучий обелиск", "Мрачная коса", "Ядовитая стрела", "Кристальный кинжал",
        "Костяной копь", "Звездный меч", "Теневой лук", "Стальной ятаган",
    ]

    def __init__(self, level=1):
        super().__init__("Оружие", randint(50, 100) / 10)
        self.name = choice(self.NAMES)
        self.level = 1 if level < 1 else level

    def __str__(self):
        return f"WEAPON ({self.name}, {self.level}, {self.mass}))"

    def __repr__(self):
        return self.__str__()


class Eat(Thing):
    def __init__(self, name, points, type, permanent, rarity):
        super().__init__("Еда", randint(2, 5) / 10)
        self.name = name
        self.points = points
        self.type = type
        self.permanent = permanent
        self.rarity = rarity

    def __str__(self):
        return f"EAT ({self.name}, {self.type}, {self.rarity}, {self.mass})"


class EatBuilder:
    EAT_PROBABILITY = 33
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


class ThingBuilder:
    def __init__(self):
        self.eat_builder = EatBuilder()

    def get_things(self, level):
        things = []
        p = randint(1, 100)
        if p <= Weapon.WEAPON_PROBABILITY:
            things.append(Weapon(level + randint(-2, 2)))
        p = randint(1, 100)
        if p <= Armor.ARMOR_PROBABILITY:
            things.append(Armor(level + randint(-2, 2)))
        p = randint(1, 100)
        if p <= EatBuilder.EAT_PROBABILITY:
            things.append(self.eat_builder.get_food())
        return things
