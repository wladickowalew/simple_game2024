from consts import *


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
        self.sum_mass -= self.things[index]
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
        print(f"""Ты заглядывешь в рюкзак, вещей: {len(things)}. 
        Масса рюкзака: {player.inventory.get_mass()}""")
        for i, thing in enumerate(things, start=1):
            print(i, thing)

    @staticmethod
    def show_equipment(player):
        weapon = player.current_weapon
        if weapon:
            print("В твеой руке сейчас:", weapon)
        else:
            print("У тебя нет оружия")
        armor = player.current_armor
        if weapon:
            print("На тебе сейчас:", armor)
        else:
            print("У тебя нет брони")


    @staticmethod
    def use_thing(player):
        thing = InventoryInterface.__get_thing(player.inventory.things)
        if thing:
            print(f"Использование предмета: {thing}")

    @staticmethod
    def delete_thing(player):
        thing = InventoryInterface.__get_thing(player.inventory.things)
        if thing:
            print(f'Вы выбросили {thing}')

    @staticmethod
    def take_thing(player):
        things = player.current_room.things
        if not things:
            print("В этой комнате нет вещей")
            return
        elif player.current_room.enemies:
            print("В этой комнате ещё есть враги")
            return
        thing = InventoryInterface.__get_thing(player.current_room.things)
        if thing:
            player.inventory.add_thing(thing)
            print(f'Вы подобрали {thing}')

    @staticmethod
    def __get_thing(things):
        length = len(things)
        if length == 0:
            print(f"У тебя нет предметов")
            return
        print(f"Выбери предмет. Введи число от 1 до {length}")
        t = input()
        if t not in [str(i) for i in range(1, length + 1)]:
            print("Неверный номер предмета")
            return
        else:
            return things.pop(int(t) - 1)


