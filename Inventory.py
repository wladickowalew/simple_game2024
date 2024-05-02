from consts import *
from Game_things import Armor, Weapon, Eat


class Inventory:
    MAX_MASS = 50

    def __init__(self):
        self.things = []
        self.sum_mass = 0

    def get_things(self):
        return self.things

    def get_mass(self):
        return self.sum_mass

    def delete_thing(self, index):
        self.sum_mass -= self.things[index].mass
        return self.things.pop(index)

    def add_thing(self, obj):
        if self.sum_mass + obj.mass >= Inventory.MAX_MASS:
            return False
        else:
            self.things.append(obj)
            self.sum_mass += obj.mass
            return True


class InventoryInterface:

    @staticmethod
    def main(player):
        while True:
            choice = input(INVENTORY_INTERFACE_TEXT)
            if choice in ['1', '2', '3', '4', '5', '6']:
                if choice == '1':
                    InventoryInterface.show_inventory(player)
                elif choice == '2':
                    InventoryInterface.show_equipment(player)
                elif choice == '3':
                    InventoryInterface.use_thing(player)
                elif choice == '4':
                    InventoryInterface.delete_thing(player)
                elif choice == '5':
                    InventoryInterface.take_thing(player)
                else:
                    break
            else:
                print("Ты ввёл что-то непонятное. Попробуй ещё раз")

    @staticmethod
    def show_inventory(player):
        things = player.inventory.get_things()
        print(f"\n\nТы заглядывешь в рюкзак, вещей: {len(things)}.")
        print(f"Масса рюкзака: {player.inventory.get_mass()}""")
        for i, thing in enumerate(things, start=1):
            print(i, thing)

    @staticmethod
    def show_equipment(player):
        print(player)
        weapon = player.current_weapon
        if weapon:
            print("В твоей руке сейчас:", weapon)
        else:
            print("У тебя нет оружия")
        armor = player.current_armor
        if armor:
            print("На тебе сейчас:", armor)
        else:
            print("У тебя нет брони")


    @staticmethod
    def use_thing(player):
        thing = InventoryInterface.__get_thing(player)
        if not thing:
            return
        print(f"Использование предмета: {thing}")
        if isinstance(thing, Armor):
            if not player.change_armor(thing):
                print("Невозможно заменить броню")
            else:
                print("Успешная замена брони, экипировано: ", thing)
        elif isinstance(thing, Weapon):
            if not player.change_weapon(thing):
                print("Невозможно заменить оружие")
            else:
                print("Успешная замена оружия, экипировано: ", thing)
        elif isinstance(thing, Eat):
            player.eat_thing(thing)
            print("Вы съели:", Eat)
        else:
            print("КАААААААК???", thing)

    @staticmethod
    def delete_thing(player):
        thing = InventoryInterface.__get_thing(player)
        if thing:
            print(f'Вы выбросили {thing}')

    @staticmethod
    def take_thing(player):
        things = player.current_room.things
        if not things:
            print("В этой комнате нет вещей")
            return
        # elif player.current_room.enemies:
        #     print("В этой комнате ещё есть враги")
        #     return
        print("В углу комнаты лежат следующие предметы:")
        for i, thing in enumerate(things, start=1):
            print(i, thing)
        print(f"Выбери предмет. Введи число от 1 до {len(things)}")
        t = input()
        if t not in [str(i) for i in range(1, len(things) + 1)]:
            print("Неверный номер предмета")
            return
        thing = things.pop(int(t) - 1)
        player.inventory.add_thing(thing)
        print(f'Вы подобрали {thing}')

    @staticmethod
    def __get_thing(player):
        length = len(player.inventory.things)
        if length == 0:
            print(f"У тебя нет предметов")
            return
        for i, thing in enumerate(player.inventory.things, start=1):
            print(i, thing)
        print(f"Выбери предмет. Введи число от 1 до {length}")
        t = input()
        if t not in [str(i) for i in range(1, length + 1)]:
            print("Неверный номер предмета")
            return
        else:
            return player.inventory.delete_thing(int(t) - 1)


