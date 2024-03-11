class GamePerson:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack

    def attack(self, other):
        if self.attack > other.hp:
            other.hp = 0
        else:
            other.hp -= self.attack

    def is_dead(self):
        return self.hp == 0


class Player(GamePerson):
    def __init__(self, name):
        super().__init__(100, 50)
        self.name = name
        self.inventory = []
        self.current_weapon = None
        self.armor_head = None
        self.armor_body = None
        self.armor_foot = None
        self.armor_arm = None


class Enemy(GamePerson):
    def __init__(self, type, attack, hp):
        super().__init__(hp, attack)
        self.type = type


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Гоблин", 25, 50)
        self.weapon = None


class Bear(Enemy):
    def __init__(self):
        super().__init__("Медведь", 80, 100)
        self.armor = None