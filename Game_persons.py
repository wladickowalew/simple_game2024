from random import randint, choice
from Inventory import Inventory
from consts import *


class GamePerson:
    def __init__(self, hp, attack):
        self.hp = hp
        self.max_hp = hp
        self.attack = attack

    def attack_other(self, other):
        if self.attack > other.hp:
            other.hp = 0
        else:
            other.hp -= self.attack
        return self.attack

    def is_dead(self):
        return self.hp <= 0

    def get_full_name(self):
        return ""


class Player(GamePerson):
    permanent_hp = 0
    permanent_attack = 0

    def __init__(self, name, room):
        super().__init__(100 + self.permanent_hp, 45 + self.permanent_attack)
        self.name = name
        self.inventory = Inventory()
        self.current_weapon = None
        self.current_armor = None
        self.current_room = room
        self.rooms_count = 1
        self.kill_count = 0
        self.points = 0

    def attack_other(self, other):
        attack = self.attack
        if self.current_weapon:
            attack += self.current_weapon.attack
        other.hp -= attack
        if self.current_weapon:
            self.current_weapon.attack -= 5
        return attack

    def get_full_name(self):
        return self.name

    def change_armor(self, new_armor):
        if self.current_armor is None:
            self.current_armor = new_armor
            return True
        if self.inventory.add_thing(self.current_armor):
            self.current_armor = new_armor
            return True
        else:
            self.inventory.add_thing(new_armor)
            return False

    def change_weapon(self, new_weapon):
        if self.current_weapon is None:
            self.current_weapon = new_weapon
            return True
        if self.inventory.add_thing(self.current_weapon):
            self.current_weapon = new_weapon
            return True
        else:
            self.inventory.add_thing(new_weapon)
            return False

    def eat_thing(self, eat):
        if eat.permanent:
            if eat.type == TYPE_HP:
                self.permanent_hp += eat.points
                self.hp += eat.points
                self.max_hp += eat.points
            elif eat.type == TYPE_ATTACK:
                self.permanent_attack += eat.points
                self.attack += eat.points
        else:
            if eat.type == TYPE_HP:
                self.hp = min(eat.points + self.hp, self.max_hp)
            elif eat.type == TYPE_ATTACK:
                self.attack += eat.points

    def __str__(self):
        return (f"Персонаж {self.name}, HP:{self.hp}/{self.max_hp}, " +
                f"Уровень атаки: {self.attack}")


class Enemy(GamePerson):
    GOBLIN_PROBABILITY = 25
    BEAR_PROBABILITY = 5

    def __init__(self, type, attack, hp):
        super().__init__(hp, attack)
        self.type = type

    def attack_other(self, other):
        if other.current_armor:
            armor = other.current_armor.hp
        else:
            armor = 0
        if self.attack > armor:
            r = self.attack - armor
        else:
            r = 0
        if other.current_armor:
            other.current_armor.hp -= 10
        other.hp -= r
        return r

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
        super().__init__("Гоблин",
                         25 + 5 * level,
                         50 + 10 * level)
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
        super().__init__("Медведь",
                         80 + 10 * level,
                         100 + 30 * level)
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
