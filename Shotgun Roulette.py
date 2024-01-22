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
        return f"Ваш ход {self.name}"
    
    def FinishMove(self):
        self.move = 0
        return "Ваш ход завершен"

    def GiveHp(self, hp_number: int):
        self.hp += hp_number

    def Status(self):
        print(f"Name = {self.name};  ", end="")
        print(f"HP = {self.hp}")


class ShotGun:
    rounds = []
    damage = -1
    
    def ShufflePellets(self, live_rounds: int, blanks: int):
        self.rounds = [1 for i in range(live_rounds)] + [0 for i in range(blanks)]
        print(self.rounds)
        random.shuffle(self.rounds)

    def Shot(self, user1: Player, user2: Player, user_shotted_name: str):
        
        if user1.move:
            user_walker = user1
            user_waiter = user2
        else:
            user_walker = user2
            user_waiter = user1 
        shot = self.rounds.pop()

        if shot and user_walker.name == user_shotted_name:
            print("ВЫСТРЕЛ, пуля была нормальная")
            user_walker.GiveHp(self.damage)
            print(user_walker.FinishMove())
            print(user_waiter.StartMove())
        elif shot and user_waiter.name == user_shotted_name: 
            print("ВЫСТРЕЛ, пуля была нормальная")
            user_waiter.GiveHp(self.damage)
            print(user_walker.FinishMove())
            print(user_waiter.StartMove())
        elif not shot and user_walker.name == user_shotted_name:
            print("ВЫСТРЕЛ, пуля была хуевая")
            pass
        elif not shot and user_waiter.name == user_shotted_name: 
            print("ВЫСТРЕЛ, пуля была хуевая")
            print(user_walker.FinishMove())
            print(user_waiter.StartMove())
        else:
            print("Вы неправильно ввели имя")
            pass
        
        if len(self.rounds) == 0:
            print("Пули закончились")
            #
            user1.Status()
            user2.Status()
            #


start_hp = 1

user1 = Player("Player1")
user1.StartHp(start_hp)
user2 = Player("Player2")
user2.StartHp(start_hp)
shotgun = ShotGun()
shotgun.ShufflePellets(1, 2)

if random.randint(0, 1):
    print(f"Первым начинает {user1.name}")
    print(user1.StartMove())
else:
    print(f"Первым начинает {user2.name}")
    print(user2.StartMove())

for command in stdin:
    command = command.rstrip("\n")
    if command == "shot":
        print("Введите имя игрока")
        shotgun.Shot(user1, user2, input())
    if command == "status":
        user1.Status()
        user2.Status()
    if command == "finish":
        break

exit()