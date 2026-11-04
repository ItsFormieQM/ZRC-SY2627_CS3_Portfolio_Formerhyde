import wrappers as wrp
class HealthPotion:
    def use(self):
        wrp.sdm("You regained 50 HP!")
class ManaPotion:
    def use(self):
        wrp.sdm("You restored 30 MP!")
class SpeedBoost:
    def use(self):
        wrp.sdm("Your speed increases for 10 seconds!")
def apply_item(item):
    for i in range(len(item)):
        item[i].use()

potions = [
    HealthPotion(),
    ManaPotion(),
    SpeedBoost()
]
apply_item(potions)
