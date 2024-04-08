from Rooms import Room
from Game_persons import Player


def choose_room(room):
    print(f"Выбери, в какой проход пойти. Введи цифру от 1 до {room.get_rooms_count()}")
    try:
        ans = int(input()) - 1
        assert 0 <= ans < room.get_rooms_count()
        return ans
    except Exception:
        print("Неверный ввод, попробуй ещё раз)")
        return choose_room(room)


def main():
    current_room = Room()
    current_room.generate_room()
    name = input("Выбери имя для своего персонажа: ")
    player = Player(name, current_room)
    while True:
        player.current_room.show_room_info()
        i = choose_room(player.current_room)
        player.current_room = player.current_room.go_to_room(i)


if __name__ == '__main__':
    main()
