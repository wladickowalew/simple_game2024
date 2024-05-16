from Rooms import Room
from Game_persons import Player
from Inventory import InventoryInterface
from BattleInterface import BattleInterface
from consts import *


def go_to_room(player):
    room = player.current_room
    print(f"Выбери, в какой проход пойти. Введи цифру от 1 до {room.get_rooms_count()}")
    try:
        ans = int(input()) - 1
        assert 0 <= ans < room.get_rooms_count()
        if player.current_room.enemies and ans != 0:
            print("Путь преграждают враги!")
            return
        else:
            if player.current_room.rooms[ans].first_enter:
                player.points += 10
                player.rooms_count += 1
            player.current_room = player.current_room.go_to_room(ans)
    except Exception:
        print("Неверный ввод, попробуй ещё раз)")
        go_to_room(player)


def main():
    current_room = Room()
    current_room.generate_room()
    name = input("Выбери имя для своего персонажа: ")
    player = Player(name, current_room)
    while not player.is_dead():
        player.current_room.show_room_info()
        choice = input(MAIN_INTERFACE_TEXT)
        if choice in ['1', '2', '3']:
            if choice == '1':
                go_to_room(player)
            elif choice == '2':
                InventoryInterface.main(player)
            else:
                if player.current_room.enemies:
                    BattleInterface.main(player)
                else:
                    print("В этой комнате не с кем драться")
        else:
            print(ERROR_INPUT_TEXT)
    print(f"Игра окончена!\nВы посетили комнат: {player.rooms_count}\n" +
          f"Убили врагов: {player.kill_count}\n" +
          f"Всего очков заработано: {player.points}")


if __name__ == '__main__':
    main()
