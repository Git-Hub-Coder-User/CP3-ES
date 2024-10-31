class Monster:
    def __init__(self):
        self.origin = None
        self.attack = None
        self.move = None
    
    def __str__(self):
        return(f"is from {self.origin} and currently has {self.attack} with {self.move}! ")

    def combat(self, other):
        print("Our challenger", self)
        print("Our defender", other)
        if self.attack > other.attack:
            self.attack += 1
            return "Victory! "
        elif self.attack < other.attack:
            other.attack += 1
            return "Loss! "
        else:
            return "Tie"
        
class Mummy(Monster):
    def __init__(self):
        super().__init__()
        self.origin = "Egypt"
        self.attack = 15
        self.move = "Mummy Tangle"

class Skeleton(Monster):
    def __init__(self):
        super().__init__()
        self.origin = "The Void"
        self.attack = 5
        self.move = "Rattle Clattle"

class Cobra(Monster):
    def __init__(self):
        super().__init__()
        self.origin = "The Amazon"
        self.attack = 17
        self.move = "Hug of Doom"

class Witch(Monster):
    def __init__(self):
        super().__init__()
        self.origin = "Swamp"
        self.attack = 25
        self.move = "Dark Magic"

Susan = Mummy()
Jack = Skeleton()
Serphant = Cobra()
Hex = Witch()

print("Susan", Susan)

print(Susan.combat(Jack))
print(Susan.combat(Serphant))
print(Susan.combat(Jack))
print(Susan.combat(Jack))
print(Susan.combat(Jack))
print(Susan.combat(Serphant))
print(Susan.combat(Hex))