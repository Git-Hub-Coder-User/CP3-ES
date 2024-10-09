""" 
These are notes about classes
"""
#Start classes with keyword class and use PascalCase

class Animal:
    #We start with the constructor which defines the attributes of the object
    def __init__(self, name, species, age, gender, rarity):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.rarity = rarity
        self.losses = 0 #This is what I did
    
    #Makes it printable and you can show it exists
    def __str__(self):
        return f"Name: {self.name} \nAge: {self.age} \nSpecies: {self.species} \nGender: {self.gender} \nRarity: {self.rarity} "
    
    #Methods are functions inside of the class
    def fight(self, other):
        if len(self.name) > len(other.name):
            other.losses += 1
            return self.name
        elif len(self.name) < len(other.name):
            self.losses += 1
            return other.name
        else:
            self.losses += 1
            other.losses += 1
            return "Tie"
    

#Creates an object of class Animal
    # We don't always want our object to be a variable i.e. We make a list/array so we can set them easier    
cat = Animal("Lyna", "Cat", 21, "Female", "Common")
frog = Animal("Bix", "Poison Dart Frog", 500, "Female", "Rare")


"""
# This is what you're supposed to do
cat.losses = 0
frog.losses = 0
"""

print(cat)
print(frog)

#To call a method you need the name of the object.name of the method and the (neccessary arguments)
print(cat.fight(frog))
print(frog.losses)
print(cat.losses)

frog.name = "Khayotick"

print(frog.fight(cat))
print(frog.losses)
print(cat.losses)

frog = None
print(frog)