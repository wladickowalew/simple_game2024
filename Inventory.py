from consts import *
from Game_things import Armor, Weapon, Eat
from Game_adapter import IOAdapter

my_print, my_input = IOAdapter.get_io_functions()

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
            choice = my_input(INVENTORY_INTERFACE_TEXT)
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
                my_print("Ты ввёл что-то непонятное. Попробуй ещё раз")

    @staticmethod
    def show_inventory(player):
        things = player.inventory.get_things()
        my_print(f"\n\nТы заглядывешь в рюкзак, вещей: {len(things)}.")
        my_print(f"Масса рюкзака: {player.inventory.get_mass()}")
        for i, thing in enumerate(things, start=1):
            my_print(f"{i} {thing}")

    @staticmethod
    def show_equipment(player):
        my_print(player)
        weapon = player.current_weapon
        if weapon:
            my_print(f"В твоей руке сейчас: {weapon}")
        else:
            my_print("У тебя нет оружия")
        armor = player.current_armor
        if armor:
            my_print(f"На тебе сейчас: {armor}")
        else:
            my_print("У тебя нет брони")


    @staticmethod
    def use_thing(player):
        thing = InventoryInterface.__get_thing(player)
        if not thing:
            return
        my_print(f"Использование предмета: {thing}")
        if isinstance(thing, Armor):
            if not player.change_armor(thing):
                my_print("Невозможно заменить броню")
            else:
                my_print(f"Успешная замена брони, экипировано: {thing}")
        elif isinstance(thing, Weapon):
            if not player.change_weapon(thing):
                my_print("Невозможно заменить оружие")
            else:
                my_print(f"Успешная замена оружия, экипировано: {thing}")
        elif isinstance(thing, Eat):
            player.eat_thing(thing)
            my_print(f"Вы съели: {thing}")
        else:
            my_print(f"КАААААААК??? {thing}")

    @staticmethod
    def delete_thing(player):
        thing = InventoryInterface.__get_thing(player)
        if thing:
            my_print(f'Вы выбросили {thing}')

    @staticmethod
    def take_thing(player):
        things = player.current_room.things
        if not things:
            my_print("В этой комнате нет вещей")
            return
        elif player.current_room.enemies:
            my_print("В этой комнате ещё есть враги")
            return
        my_print("В углу комнаты лежат следующие предметы:")
        for i, thing in enumerate(things, start=1):
            my_print(i, thing)
        my_print(f"Выбери предмет. Введи число от 1 до {len(things)}")
        t = my_input()
        if t not in [str(i) for i in range(1, len(things) + 1)]:
            my_print("Неверный номер предмета")
            return
        thing = things.pop(int(t) - 1)
        player.inventory.add_thing(thing)
        my_print(f'Вы подобрали {thing}')

    @staticmethod
    def __get_thing(player):
        length = len(player.inventory.things)
        if length == 0:
            my_print(f"У тебя нет предметов")
            return
        for i, thing in enumerate(player.inventory.things, start=1):
            my_print(i, thing)
        my_print(f"Выбери предмет. Введи число от 1 до {length}")
        t = my_input()
        if t not in [str(i) for i in range(1, length + 1)]:
            my_print("Неверный номер предмета")
            return
        else:
            return player.inventory.delete_thing(int(t) - 1)


