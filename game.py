from componets import *
from sys import stdin
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



for round in range(3): # NOT READY 
    shotgun.ShufflePellets(pellets_variants[round])

    while user1.hp != 0 and user2.hp != 0:
        attacker_name = ChangeTurn(user1, user2)
        print(f"It's {attacker_name} turn")

        for command in stdin:
            command = command.rstrip("\n")

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
            
        
    print(GameStatus(user1, user2))

    shotgun.RemoveTrim()
    break


