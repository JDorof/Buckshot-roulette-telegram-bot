from componets import *


user1 = Player('p1')
user2 = Player('p2')
shotgun = ShotGun()

pellets_variants = {
    (1, 2)
    (3, 2)
    (3, 4)
    (2, 3)
    (4, 4)
}

#===================================# use randint to choose first player randomly
user2.turn = 1
#===================================#

for round in range(3):
    shotgun.ShufflePellets(pellets_variants[round])
    while user1.hp != 0 or user2.hp != 0:
        attacker_name = ChangeTurn(user1, user2)
        print(f"It's {attacker_name} turn")





        break
    break


