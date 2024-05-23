from random import randint
from Game_things import ThingBuilder
from Game_persons import EnemyBuilder


class Room:
    __N = 1
    __THING_BUILDER = ThingBuilder()
    __ENEMY_BUILDER = EnemyBuilder()

    def __init__(self, level=1):
        self.num = Room.__N
        Room.__N += 1
        self.level = level
        if self.num == 1:
            self.enemies = []
        else:
            self.enemies = self.__ENEMY_BUILDER.get_enemies(level // 2)
        self.things = self.__THING_BUILDER.get_things(level // 2)
        self.rooms = []
        self.first_enter = True

    def generate_room(self, from_room=-1):
        rooms_count = randint(1, 3)
        if from_room != -1:
            self.rooms.append(from_room)
        for i in range(rooms_count):
            self.rooms.append(Room(self.level + 1))

    def get_rooms_count(self):
        return len(self.rooms)

    def go_to_room(self, index):
        new_room = self.rooms[index]
        self.first_enter = False
        if new_room.first_enter:
            new_room.generate_room(from_room=self)
        return new_room

    def __str__(self):
        s = f"\nКомната № {self.num}\n"
        if self.first_enter:
            s += "Вы здесь впервые\n"
        else:
            s += "Вы здесь уже были\n"
        s += f"Враги: {' '.join(str(e) for e in self.enemies)}\n"
        s += f"Лут: {' '.join(str(e) for e in self.things)}\n"
        s += f"Количество выходов из комнаты: {len(self.rooms)}"
        return s
