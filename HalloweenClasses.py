class Monster:
    def __init__(self):
        self.origin = None
        self.attack = None
        self.move = None
        self.name = None
    
    def __str__(self):
        return(f"{self.name} is from {self.origin} and currently has {self.attack} attack with {self.move}! ")

    def combat(self, other):
        print(f"Our challenger", self)
        print(f"Our defender", other, "\n")
        if self.attack > other.attack:
            self.attack += 1
            return f"{self.name} won! They are strengthened by their victory. \n"
        elif self.attack < other.attack:
            other.attack += 1
            return f"{other.name} won! They are strengthened by their victory. \n"
        else:
            return "Tie\n"
        
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
        self.origin = "the Void"
        self.attack = 5
        self.move = "Rattle Clattle"
        self.name = name

class Cobra(Monster):
    def __init__(self, name):
        super().__init__()
        self.origin = "the Amazon"
        self.attack = 17
        self.move = "Hug of Doom"
        self.name = name

class Witch(Monster):
    def __init__(self, name):
        super().__init__()
        self.origin = "the Swamp"
        self.attack = 25
        self.move = "Dark Magic"
        self.name = name


def enemies(enemies):
    for enemy in enemies:
        print(enemy)
    print("")

for i in range(1):
    print("This is a very simple game and allows for rat farming. ")
    print("Let's be real. We've all been guilty of rat farming at some point. \n")
    print("To win the game, you need to beat Hex, the witch from the swamp. After that, the game will end. ")
    print("Now, let's get started. \n")


user = input("Name your monster! ").capitalize()

while True: 
    inputed = input(f"Is {user} a mummy, a skeleton, a cobra or a witch? ").lower().strip()
    if inputed == "mummy":
        user = Mummy(user)
    elif inputed == "skeleton":
        user = Skeleton(user)
        user.attack += 1
    elif inputed == "cobra":
        user = Cobra(user)
    elif inputed == "witch":
        user = Witch(user)
    else:
        print("Invalid option, please try again! ")
        continue
    break

print(f"{user.name} is now ready for combat! ")
print("\n")


susan = Mummy("Susan")
jack = Skeleton("Jack")
jerry = Skeleton("Jerry")
serphant = Cobra("Serphant")
hex = Witch("Hex")


while True:
    print(user)
    print()
    enemies([susan, jack, jerry, serphant, hex])
    inputed = input("Who would you like to fight? ").capitalize().strip()
    if inputed == "Susan":
        print(user.combat(susan))
    elif inputed == "Jack":
        print(user.combat(jack))
    elif inputed == "Jerry":
        print(user.combat(jerry))
    elif inputed == "Serphant":
        print(user.combat(serphant))
    elif inputed == "Hex":
        string = user.combat(hex)
        print(string)
        if user.name in string:
            print("You beat Hex! You won the game! Great job! ")
            break
    else:
        print("Invalid option")