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

    def Status(self): # TODO return f"..."
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
        self.status = 1
        live_pellets = pellets[0]
        blanks = pellets[1]
        pellets = [1 for i in range(live_pellets)] + [0 for i in range(blanks)]
        self.pellets = pellets[:]
        random.shuffle(self.pellets)
        return pellets

    def Shot(self):
        if not self.status:
            return 0
        return self.pellets.pop()


    def Trim(self):
        self.damage = 2
        return "damage = 2"
        # self.trim = 1
    
    def RemoveTrim(self):
        self.damage = 1
        return "damage = 1"
        # self.trim = 0


def GameStatus(user1: Player, user2: Player): # TODO return variable (not full str)
    hp1 = "♥" * user1.hp
    hp2 = "♥" * user2.hp
    line = "="*16
    return f"{line}\n{user1.name:<8}{user2.name:>8}\n{hp1:<8}{hp2:>8}\n{line}"


def ChangeTurn(user1: Player, user2: Player):
    if user1.turn:
        user1.turn = 0
        user2.turn = 1
        return user2.name
    elif user2.turn:
        user1.turn = 1
        user2.turn = 0
        return user1.name


def Shot(user1: Player, user2: Player, attacker_name: str, target_name: str, shotgun: ShotGun):
    if user1.name != target_name and user2.name != target_name:
        print("Incorrect name")
        return 0
    if shotgun.Shot():
        print("BADUM")
        if user1.name == target_name:
            user1.Damage(shotgun.damage)
        elif user2.name == target_name:
            user2.Damage(shotgun.damage)
        return 1
    else:
        print("BLANK")
        if user1.name == attacker_name:
            if user1.name == target_name:
                return 0
            elif user2.name == target_name:
                return 1
        if user2.name == attacker_name:
            if user2.name == target_name:
                return 0
            elif user1.name == target_name:
                return 1
   