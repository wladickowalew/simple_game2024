from Game_things import Thing


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

    def add_thing(self, obj: Thing):
        if self.sum_mass + obj.mass >= Inventory.MAX_MASS:
            return False
        else:
            self.things.append(obj)
            self.sum_mass += obj.mass
            return True
