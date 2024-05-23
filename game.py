from Rooms import Room
from Game_persons import Player
from Inventory import InventoryInterface
from BattleInterface import BattleInterface
from sql_connector import SqlConnector
from Game_adapter import IOAdapter
from consts import *

my_print, my_input = IOAdapter.get_io_functions()


def go_to_room(player):
    room = player.current_room
    my_print(f"Выбери, в какой проход пойти. Введи цифру от 1 до {room.get_rooms_count()}")
    try:
        ans = int(my_input()) - 1
        assert 0 <= ans < room.get_rooms_count()
        if player.current_room.enemies and ans != 0:
            my_print("Путь преграждают враги!")
            return
        else:
            if player.current_room.rooms[ans].first_enter:
                player.points += 10
                player.rooms_count += 1
            player.current_room = player.current_room.go_to_room(ans)
    except Exception:
        my_print("Неверный ввод, попробуй ещё раз)")
        go_to_room(player)


def main(name, tg_id):
    SqlConnector.init()
    current_room = Room()
    current_room.generate_room()
    player = Player(name, current_room)
    while not player.is_dead():
        my_print(player.current_room)
        choice = my_input(MAIN_INTERFACE_TEXT)
        if choice in ['1', '2', '3']:
            if choice == '1':
                go_to_room(player)
            elif choice == '2':
                InventoryInterface.main(player)
            else:
                if player.current_room.enemies:
                    BattleInterface.main(player)
                else:
                    my_print("В этой комнате не с кем драться")
        else:
            my_print(ERROR_my_input_TEXT)
    game_over(player)


def game_over(player):
    SqlConnector.update_user(player.tg_id, player.permanent_attack, player.permanent_hp)
    my_print(f"\nИгра окончена!\nВы посетили комнат: {player.rooms_count}\n" +
             f"Убили врагов: {player.kill_count}\n" +
             f"Всего очков заработано: {player.points}")
    SqlConnector.add_record(player.tg_id,
                            player.rooms_count,
                            player.kill_count,
                            player.points,
                            0)
    show_user_statistic(player)
    show_all_statistic()


def show_user_statistic(player):
    columns = ["Имя", "Комнат", "Убийств", "Очков"]
    data_u = SqlConnector.read_stat_for_user(player.tg_id)
    my_print("\nВаша Статистика:")
    my_print("\t".join(i.ljust(10, " ") for i in columns))
    for tr in data_u:
        my_print("\t".join(str(i).ljust(10, " ") for i in tr[:-1]))


def show_all_statistic():
    columns = ["Имя", "Комнат", "Убийств", "Очков"]
    data_all = SqlConnector.read_stat_by_points()
    my_print("\nВcя Статистика:")
    my_print("\t".join(i.ljust(10, " ") for i in columns))
    for tr in data_all:
        my_print("\t".join(str(i).ljust(10, " ") for i in tr[:-1]))
