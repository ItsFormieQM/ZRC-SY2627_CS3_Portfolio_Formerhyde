import wrappers as wrp
class Warrior:
    def special_move(self):
        wrp.sdm("Warrior swings a mighty sword!")
class Mage:
    def special_move(self):
        wrp.sdm("Mage casts a powerful spell!")
    pass
class Archer:
    def special_move(self):
        wrp.sdm("Archer shoots a precise arrow!")
    pass

def perform_move(character):
    character.special_move()

characters = [
    Warrior(),
    Mage(),
    Archer()
]

for i in range(len(characters)):
    perform_move(characters[i])