from consts import *
from random import randint
from Game_persons import Bear, Goblin
from Game_adapter import IOAdapter

my_print, my_input = IOAdapter.get_io_functions()


class BattleInterface:
    enemies = []
    escape = False

    @staticmethod
    def main(player):
        my_print(BATTLE_INERFACE_TEXT_BEGIN)
        BattleInterface.escape = False
        BattleInterface.enemies = player.current_room.enemies
        if len(BattleInterface.enemies) < 3:
            lenta = [player] + BattleInterface.enemies[::]
        else:
            lenta = ([player] + BattleInterface.enemies[:2] +
                     [player] + [BattleInterface.enemies[2]])
        counter = -1
        while not (player.is_dead() or (not BattleInterface.enemies) or BattleInterface.escape):
            counter = (counter + 1) % len(lenta)
            q = lenta[counter]
            if q == player:
                my_print("Очередь Боя:", " -> ".join([p.get_full_name() for p in lenta]))
                enemy = BattleInterface.step_user(player)
                if not (enemy is None):
                    lenta.remove(enemy)
            else:
                BattleInterface.step_enemy(q, player)
        my_print("Бой окончен")


    @staticmethod
    def step_user(player):
        enemies = BattleInterface.enemies
        while True:
            n = len(enemies)
            p = 100 - 25 * n
            BattleInterface.show_text(enemies)
            choice = my_input(BATTLE_INERFACE_TEXT_END)
            if choice not in [str(i) for i in range(1, n + 2)]:
                my_print("Ты ввёл что-то непонятное. Попробуй ещё раз")
                continue
            k = int(choice)
            if k == n + 1:
                if randint(1, 100) < p:
                    my_print("Вы успешно сбежали")
                    BattleInterface.escape = True
                else:
                    my_print("Неудачная попытка бегства(((")
                break
            else:
                a = player.attack_other(enemies[k - 1])
                my_print(f"Вы атакуете врага на {a} очков")
                if player.current_weapon:
                    if player.current_weapon.attack <= 0:
                        player.current_weapon = None
                        my_print("Вашe стало тупее тупого угла")
                    else:
                        my_print(f"Ваша оружее немного затупилось о броню врага. {player.current_weapon.attack}")
                if enemies[k - 1].is_dead():
                    my_print("Враг повержен!")
                    player.kill_count += 1
                    if isinstance(enemies[k - 1], Bear):
                        player.points += 10 * enemies[k - 1].level
                    elif isinstance(enemies[k - 1], Goblin):
                        player.points += 5 * enemies[k - 1].level
                    return enemies.pop(k - 1)
                else:
                    return None


    @staticmethod
    def step_enemy(enemy, player):
        a = enemy.attack_other(player)
        my_print(f"Враг {enemy} атакует вас на {a} очков")
        if not player.current_armor:
            return
        if player.current_armor.hp <= 0:
            player.current_armor = None
            my_print("Ваша броня разрушена. Больше она вас не защищает")
        else:
            my_print(f"Ваша броня пострадала, текущее хп брони: {player.current_armor.hp}")

    @staticmethod
    def show_text(enemies):
        n = len(enemies)
        my_print("Перед вами стоят враги:")
        for enemy in enemies:
            my_print(enemy)
        my_print("Ваши действия: ")
        for i, enemy in enumerate(enemies, 1):
            my_print(f"{i}) Атаковать {enemy}")
        p = 100 - 25 * n
        my_print(f"{n + 1}) сбежать (вероятность {p}%)")
