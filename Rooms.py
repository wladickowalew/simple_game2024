from random import randint
from Game_things import ThingBuilder
from Game_persons import EnemyBuilder


class Room:
    __N = 1
    __THING_BUILDER = ThingBuilder()
    __ENEMY_BUILDER = EnemyBuilder()

    def __init__(self):
        self.num = Room.__N
        Room.__N += 1
        self.enemies = self.__ENEMY_BUILDER.get_enemies(5)
        self.things = self.__THING_BUILDER.get_things(5)
        self.rooms = []
        self.first_enter = True

    def generate_room(self, from_room=-1):
        rooms_count = randint(1, 3)
        if from_room != -1:
            self.rooms.append(from_room)
        for i in range(rooms_count):
            self.rooms.append(Room())

    def get_rooms_count(self):
        return len(self.rooms)

    def go_to_room(self, index):
        new_room = self.rooms[index]
        self.first_enter = False
        if new_room.first_enter:
            new_room.generate_room(from_room=self)
        return new_room

    def show_room_info(self):
        print("Комната №", self.num)
        if self.first_enter:
            print("Вы здесь впервые")
        else:
            print("Вы здесь уже были")
        print("Враг:", *self.enemies, sep=", ")
        print("Лут:", *self.things, sep=", ")
        print("Количество выходов из комнаты:", len(self.rooms))
