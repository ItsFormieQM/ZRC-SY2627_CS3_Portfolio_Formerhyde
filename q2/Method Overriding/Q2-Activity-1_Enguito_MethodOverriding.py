class Animal:
    def __init__(self,name):
        self.__name = name
        other_name = self.get_name()
        self.name = other_name # // somehow it works lol
    def make_sound(self):
        print(f"{self.__name} made sound.")
    def eat(self):
        print(f"{self.__name} ate.")
    def get_name(self):
        return self.__name
    def info(self):
        print(f"Class Name: {self.__class__.__name__}")
        print(f"Name: {self.__name}")
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name} roars loudly!")
    def eat(self):
        print(f"{self.name} eats fresh meat.")
class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} trumpets!")
    def eat(self):
        print(f"{self.name} eats grass and fruits.")
class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} chatters!")
    def eat(self):
        print(f"{self.name} eats bananas.")
print("---Animal Zoo Showcase---")
print()
simba = Lion("Simba")
simba.make_sound()
simba.eat()
print()
elephant = Elephant("Dumbo")
elephant.make_sound()
elephant.eat()
print()
jared = Monkey("Jared")
jared.make_sound()
jared.eat()
    