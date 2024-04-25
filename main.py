from Rooms import Room
from Game_persons import Player
from Inventory import InventoryInterface
from consts import *


def go_to_room(player):
    room = player.current_room
    print(f"Выбери, в какой проход пойти. Введи цифру от 1 до {room.get_rooms_count()}")
    try:
        ans = int(input()) - 1
        assert 0 <= ans < room.get_rooms_count()
        player.current_room = player.current_room.go_to_room(ans)
    except Exception:
        print("Неверный ввод, попробуй ещё раз)")
        go_to_room(room)


def main():
    current_room = Room()
    current_room.generate_room()
    name = input("Выбери имя для своего персонажа: ")
    player = Player(name, current_room)
    while True:
        player.current_room.show_room_info()
        choice = input(MAIN_INTERFACE_TEXT)
        if choice in ['1', '2', '3']:
            if choice == '1':
                go_to_room(player)
            elif choice == '2':
                InventoryInterface.main(player)
            else:
                print('начинается битва')
        else:
            print(ERROR_INPUT_TEXT)


if __name__ == '__main__':
    main()
