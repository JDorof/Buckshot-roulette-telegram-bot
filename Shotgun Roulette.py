import random
from sys import stdin


class Player:
    name = ""
    hp = 1
    items = {
        '1': None,
        '2': None,
        '3': None,
        '4': None,
        '5': None,
        '6': None,
        '7': None,
        '8': None,
    }
    move = 0

    def __init__(self, name):
        self.name = name

    def StartHp(self, hp_number: int):
        self.hp = hp_number
    
    def StartMove(self):
        self.move = 1
        return f"Your turn {self.name}"
    
    def FinishMove(self):
        self.move = 0
        return "Your turn is complete"

    def GiveHp(self, hp_number: int):
        self.hp += hp_number

    def Status(self):
        print(f"Name = {self.name};  ", end="")
        print(f"HP = {self.hp}")


class ShotGun:
    pellets = []
    damage = -1
    status = 0

    def Status(self):
        self.status = 1 if len(self.pellets) != 0 else 0
        return self.status

    def ShufflePellets(self, live_pellets: int, blanks: int):
        pellets = [1 for i in range(live_pellets)] + [0 for i in range(blanks)]
        self.pellets = [pellet for pellet in pellets]
        random.shuffle(self.pellets)
        return pellets

    def Pellets(self):
        return self.pellets

    def Shot(self):
        if not self.status:
            print("No pellets in shotgun")
            return None
        return self.pellets.pop()

shotgun = ShotGun()
print(shotgun.ShufflePellets(2, 1))
print(shotgun.Pellets())
print(shotgun.Status())
print(shotgun.Shot())

print(shotgun.Pellets())
print(shotgun.Status())
print(shotgun.Shot())

print(shotgun.Pellets())
print(shotgun.Status())
print(shotgun.Shot())

print(shotgun.Pellets())
print(shotgun.Status())
print(shotgun.Shot())


