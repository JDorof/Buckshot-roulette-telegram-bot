import random
from tracemalloc import start
import telebot


ITEMS = ['saw', 'beer', 'magnifying_glass', 'handcuffs', 'cigarettes']


class Player:
    def __init__(self, name: str, user_id):
        self.name = name
        self.hp = 0
        self.items = []
        self.user_id = user_id  # user's ID from telebot


    def GetID(self):
        return self.user_id


    def SetName(self, new_name: str) -> str:
        self.name = new_name
        return self.name
    
    
    def GetItems(self) -> list:
        return self.items


    def UseItem(self, new_item: list) -> list:
        if new_item in self.items:
            del self.items[self.items.index(new_item)]
            return self.items
        return None


    def ClearItems(self):
        self.items.clear()
        return self.items



    def AddItems(self, count: int) -> list:
        new_items = [random.choice(ITEMS) for i in range(count)]  # генерируем случайные предметы количества count

        if len(new_items) + len(self.items) > 8:
            complement = 8 - len(self.items)
            new_items = new_items[:complement]

        self.items.extend(new_items)
        return new_items


    def SetHP(self, new_hp: int) -> int:
        self.hp = new_hp
        return self.hp


    def Heal(self) -> int:
        self.hp += 1
        return self.hp


    def Damage(self, damage: int) -> int:
        self.hp -= damage
        return max(0, self.hp)


    def Status(self) -> None: # TODO return f"..."
        print(f"Name = {self.name};  ", end="")
        print(f"HP = {self.hp}")


class Game:
    def __init__(self, name_1, name_2, user_id_1, user_id_2):
        self.player_1 = Player(name_1, user_id_1)
        self.player_2 = Player(name_2, user_id_2)
        self.shotgun = ShotGun()
        self.round = 0
        self.turn = random.choice([self.player_1, self.player_2])  # who will go first
        self.opponent = self.player_1 if self.turn == self.player_2 else self.player_2
        self.current_pellet = -1  # 1 = live round, 0 = blank
        self.is_handcuffs_used = False


    def StartNewRound(self):
        """This function starts a new round, sets the starting HP for each player, and clears their inventories."""
        self.round += 1
        start_hp = self.round * 2  # The amount of HP depend on the current round
        self.player_1.SetHP(start_hp)
        self.player_2.SetHP(start_hp)
        self.player_1.ClearItems()
        self.player_2.ClearItems()


    def IsMyTurn(self, user_id):
        return self.turn.GetID() == user_id


    def LoadPellet(self, hard=False):
        """Load a new pellet or keep the already loaded one.
        
        If parameter `hard` is True, function load a new pellet anyway."""
        if self.current_pellet == -1 or hard:
            self.current_pellet = self.shotgun.GetPellet()


    def Shot(self, who: str):
        """variable `who` might be either to_opponent or to_myself"""
        
        match who:
            case 'to_opponent':
                if self.current_pellet == 1:
                    self.opponent.Damage(self.shotgun.damage)
                if not self.is_handcuffs_used:
                    self.ChangeTurn()
                self.is_handcuffs_used = False
            
            case 'to_myself':
                if self.current_pellet == 1:
                    self.turn.Damage(self.shotgun.damage)
                    if not self.is_handcuffs_used:
                        self.ChangeTurn()
                    self.is_handcuffs_used = False
        
        
        # Remove all changes from the first player
        self.shotgun.SetDamage(1)
        self.current_pellet = -1
    
    
    def ChangeTurn(self):
        self.turn, self.opponent = self.opponent, self.turn

    
    def GetPlayerByID(self, user_id):
        if self.player_1.GetID() == user_id:
            return self.player_1
        elif self.player_2.GetID() == user_id:
            return self.player_2
    
    
    def WhoWin(self):
        if self.player_1.hp == 0:
            return self.player_2
        elif self.player_2.hp == 0:
            return self.player_1
        
        return None


class ShotGun:
    def __init__(self):
        self.pellets = []  # 1 = live round, 0 = blank
        self.damage = 1


    def GetPellets(self):
        return self.pellets


    def Charge(self) -> list:
        live_round = random.randint(1, 5)
        # хочется, чтобы холостых было примерно столько же, сколько настоящих, при этом не меньше 1 и чтобы в сумме было не больше 8
        blank = min(max(1, live_round + random.randint(-2, 2)), 8 - live_round)
        self.pellets = [1 for _ in range(live_round)] + [0 for _ in range(blank)]
        random.shuffle(self.pellets)
        return self.pellets


    def IsEmpty(self) -> bool:
        return len(self.pellets) == 0


    def GetPellet(self):
        return self.pellets.pop()


    def SkipPellet(self):
        return self.pellets.pop()


    def SetDamage(self, damage: int) -> int:
        self.damage = damage
        return self.damage