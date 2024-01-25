from componets import *
from sys import stdin
import random
import time

user1 = Player("p1")
user2 = Player("p2")
shotgun = ShotGun()

pellets_variants = (
    (1, 2),
    (3, 2),
    (3, 4),
    (2, 3),
    (4, 4)
)
#===================================# use randint to choose first player randomly
user2.turn = 1
#===================================# ♡ 9825 | ♥ 9829


user1.StartHp(3)
user2.StartHp(3)


for round in range(3): # NOT READY 
    print(shotgun.ShufflePellets(pellets_variants[round]))

    while user1.hp != 0 and user2.hp != 0:
        attacker_name = ChangeTurn(user1, user2)
        print(f"It's {attacker_name} turn")

        for command in stdin:
            command = command.rstrip("\n")

            if not shotgun.Status():
                id_pellets = random.randint(0, 5)
                print(shotgun.ShufflePellets(pellets_variants[id_pellets])) 

            # bags with stdin or something
            # if code from 36str put after alls elifs, it won't work (because if we shot oursefl with blank, it would'n reload shotgun)
            # if here, you will see pellets after shot, before you can write the name

            if command == "help":
                print("shot status magnifier")
                continue

            elif command == "shot":
                print("Choose player")
                if Shot(user1, user2, attacker_name, input().rstrip("\n"), shotgun):
                    break

            elif command == "status":
                print(GameStatus(user1, user2))
                continue

            elif command == "magnifier":
                print(shotgun.ShowPellet()) # change
                continue

            elif command == "saw":
                print(shotgun.Trim())
                continue
            
            elif command == "beer":
                print(shotgun.SkipPellet()) 

        shotgun.RemoveTrim()

        
    print(GameStatus(user1, user2))

    break


