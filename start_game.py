from Game_adapter import IOAdapter
IOAdapter.init("console")

from game import main

if __name__ == '__main__':
    IOAdapter.init("console")
    name = input("Выбери имя для своего персонажа: ")
    main(name, name)
