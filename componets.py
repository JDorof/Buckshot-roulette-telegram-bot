import random


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
    turn = 0
    wins = 0

    def __init__(self, name: str):
        self.name = name

    def StartHp(self, start_hp: int):
        self.hp = start_hp
        return self.hp
    
    def NextTurn(self):
        if self.turn:
            self.turn = 0
            return self.turn
        self.turn = 1
        return self.turn

    def Heal(self):
        self.hp += 1
        return self.hp
    
    def Damage(self, damage):
        self.hp -= damage
        return self.hp

    def Status(self):
        print(f"Name = {self.name};  ", end="")
        print(f"HP = {self.hp}")


class ShotGun:
    pellets = []
    damage = 1
    # trim = 0
    status = 0

    # def Pellets(self):
    #     return self.pellets

    def ShowPellet(self):
        if not self.status:
            print("No pellets in shotgun")
            return None
        return self.pellets[-1]

    def Status(self):
        self.status = 1 if len(self.pellets) != 0 else 0
        return self.status

    def ShufflePellets(self, pellets: tuple):
        live_pellets = pellets[0]
        blanks = pellets[1]
        pellets = [1 for i in range(live_pellets)] + [0 for i in range(blanks)]
        self.pellets = [pellet for pellet in pellets]
        random.shuffle(self.pellets)
        return pellets

    def Shot(self):
        if not self.status:
            print("No pellets in shotgun")
            return None
        if self.pellets.pop():
            return self.damage
        return 0

    def Trim(self):
        self.damage = 2
        # self.trim = 1
    
    def RemoveTrim(self):
        self.damage = 1
        # self.trim = 0


def GameStatus():
    pass


def ChangeTurn(user1: Player, user2: Player):
    if user1.turn:
        user1.turn = 0
        user2.turn = 1
        return user2.name
    elif user2.turn:
        user1.turn = 1
        user2.turn = 0
        return user1.name


def Shot(attacker_name, target_name, shotgun):
    pass    