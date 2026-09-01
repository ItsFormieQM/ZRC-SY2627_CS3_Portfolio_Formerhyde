def isinteger(_val = "noone"):
    if _val == "noone":
        return -1
    try:
        _val -= 1
        return True
    except ValueError:
        return False


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        if isinteger(self.hp) == False:
            return -1
        pass
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= -9999:
            self.hp = "SWOONED"

Kris = Player("Kris", 240)
Susie = Player("Kris", 320)

print(f"Player Kris was instantiated! Starting at HP {Kris.hp}")
print(f"Player Susie was instantiated! Starting at HP {Susie.hp}")  

damage_amnt = int(input("\nHow much damage should Kris get: "))
Kris.take_damage(damage_amnt)
damage_amnt = int(input("How much damage should Susie get: "))
Susie.take_damage(damage_amnt)

print(f"Kris took damage, their HP is now {Kris.hp}")    
print(f"Susie took damage, their HP is now {Susie.hp}")   