
class pokemon:

    def __init__(self, name, hp, typ, lvl):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.lvl = lvl

    const = 0

    def __str__(self):
        return f"""
Name: {self.name} 
Type: {(self.typ).capitalize()}
Level: {self.lvl}
HP: {self.hp}
"""
    
    def combat(self, other):
        if self.lvl > other.lvl:
            return f"{self.name} won! "
        elif self.lvl < other.lvl:
            return f"{other.name} defeated {self.name}! "
        else:
            return "It's a tie. "
        
    def lvl_up(self):
        self.lvl += 1
        self.hp += 10

    # @classmethod #Can't affect an instance variable, just affects the whole class

    @classmethod
    def pikachu(self, name):
        return pokemon(name, 50, "electric", 1)
        # return pokemon(input("Give me a name: "), 50, "electric", 1) also works
    
    #Static methods do not require self or class, can work when you're dealing with multiple instances
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5

eevee = pokemon("Lexa", 50, "normal", 1)
print(eevee)
flareon = pokemon("Rachelle", 100, "fire", 10)
print(flareon)

print(eevee.combat(flareon) + "\n")

print(eevee)
eevee.lvl_up()
print(eevee)

pika = pokemon.pikachu("Lexi")
print(pika)
pika.hp = pokemon.hp_update(pika)
print(pika)