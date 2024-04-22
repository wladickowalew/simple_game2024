from random import randint, choice
from Inventory import Inventory
from Rooms import Room


class GamePerson:
    def __init__(self, hp, attack):
        self.hp = hp
        self.max_hp = hp
        self.attack = attack

    def attack(self, other):
        if self.attack > other.hp:
            other.hp = 0
        else:
            other.hp -= self.attack

    def is_dead(self):
        return self.hp == 0


class Player(GamePerson):
    def __init__(self, name, room: Room):
        super().__init__(100, 50)
        self.name = name
        self.inventory = Inventory()
        self.current_weapon = None
        self.current_armor = None
        self.current_room = room
        # self.armor_head = None
        # self.armor_body = None
        # self.armor_foot = None
        # self.armor_arm = None


class Enemy(GamePerson):
    GOBLIN_PROBABILITY = 25
    BEAR_PROBABILITY = 5

    def __init__(self, type, attack, hp):
        super().__init__(hp, attack)
        self.type = type

    def get_full_name(self):
        return ""

    def __str__(self):
        return self.get_full_name() + f" HP: {self.hp}/{self.max_hp}"

    def __repr__(self):
        return self.__str__()


class Goblin(Enemy):
    NAMES = ['Грязнуля', 'Клыкач', 'Ушастик', 'Щупальце',
             'Хватюня', 'Колючка', 'Вонючек', 'Глазобой',
             'Камнедроб', 'Зубогрыз', 'Пыхтун', 'Прищур',
             'Грызло', 'Клепанец', 'Коготун', 'Шмыгун',
             'Лапосун', 'Острозуб', 'Бешенец', 'Скитунец']

    def __init__(self, level):
        super().__init__("Гоблин", 25, 50)
        self.weapon = None
        self.name = choice(self.NAMES)
        self.level = level

    def get_full_name(self):
        return self.type + " " + self.name


class Bear(Enemy):
    NAMES = ['Клыкастый', 'Медвежий', 'Огромный', 'Грозный',
             'Кровавый', 'Бесстрашный', 'Звериный', 'Полосатый',
             'Ледяной', 'Сокрушительный', 'Гривастый', 'Лютый',
             'Ужасный', 'Могучий', 'Строгий', 'Бурый',
             'Хищный', 'Монстрозный', 'Гордый', 'Дикий']

    def __init__(self, level):
        super().__init__("Медведь", 80, 100)
        self.armor = None
        self.name = choice(self.NAMES)
        self.level = level

    def get_full_name(self):
        return self.name + " " + self.type


class EnemyBuilder:

    def get_enemies(self, level):
        enemies = []
        for i in range(3):
            p = randint(1, 100)
            if p <= Enemy.GOBLIN_PROBABILITY:
                enemies.append(Goblin(level + randint(-2, 2)))
        p = randint(1, 100)
        if p <= Enemy.BEAR_PROBABILITY:
            enemies.append(Bear(level + randint(-2, 2)))

        return enemies
