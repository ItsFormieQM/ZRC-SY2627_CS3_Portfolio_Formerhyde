class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def take_damage(self, amount):
        self.hp -= amount
        # if self.hp <= -9999:
        # self.hp = "SWOONED"
        # elif self.hp <= 0:
        # self.hp = "DOWNED"

Arthur = Hero("Arthur", 240)
Morgan = Hero("Morgan", 320)

print(f"Player Arthur was instantiated! Starting at HP {Arthur.hp}")
print(f"Player Morgan was instantiated! Starting at HP {Morgan.hp}")  

damage_amnt = 239
Arthur.take_damage(damage_amnt)
damage_amnt = 320
Morgan.take_damage(damage_amnt)

print(f"Arthur took damage, their HP is now {Arthur.hp}")    
print(f"Morgan took damage, their HP is now {Morgan.hp}")   