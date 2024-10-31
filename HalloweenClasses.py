class Monster:
    def __init__(self):
        self.origin = None
        self.attack = None
        self.move = None
        self.name = None
    
    def __str__(self):
        return(f"is from {self.origin} and currently has {self.attack} with {self.move}! ")

    def combat(self, other):
        print(f"Our challenger, {self.name},", self)
        print(f"Our defender, {other.name},", other)
        if self.attack > other.attack:
            self.attack += 1
            return f"{self.name} won! "
        elif self.attack < other.attack:
            other.attack += 1
            return f"{other.name} won! "
        else:
            return "Tie"
        
class Mummy(Monster):
    def __init__(self, name):
        super().__init__()
        self.origin = "Egypt"
        self.attack = 15
        self.move = "Mummy Tangle"
        self.name = name

class Skeleton(Monster):
    def __init__(self, name):
        super().__init__()
        self.origin = "The Void"
        self.attack = 5
        self.move = "Rattle Clattle"
        self.name = name

class Cobra(Monster):
    def __init__(self, name):
        super().__init__()
        self.origin = "The Amazon"
        self.attack = 17
        self.move = "Hug of Doom"
        self.name = name

class Witch(Monster):
    def __init__(self, name):
        super().__init__()
        self.origin = "Swamp"
        self.attack = 25
        self.move = "Dark Magic"
        self.name = name

Susan = Mummy("Susan")
Jack = Skeleton("Jack")
Serphant = Cobra("Serphant")
Hex = Witch("Hex")

print("Susan", Susan)

print(Susan.combat(Jack))
print(Susan.combat(Serphant))
print(Susan.combat(Jack))
print(Susan.combat(Jack))
print(Susan.combat(Jack))
print(Susan.combat(Serphant))
print(Susan.combat(Hex))