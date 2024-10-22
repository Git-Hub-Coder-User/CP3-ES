#How to build a subclass in python
#"That's a recursion error, not a reptile. " - LaRose
#"We will make them eat. There is no option. " - LaRose
#"See? They whine. They whine so much. " - LaRose
#Birds are birds - LaRose
#Are fish birds - Eli
#Get the birds - LaRose
#We want to keep it simple, stupid = LaRose
#I can't read anymore - LaRose

class PetStore():
    name = "PetStore"
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []
        self.featured_pet = None
    
    def add_pet(self, animal):
        #Assert checks if a statement is true; if the statement is false, it causes an error
        #Is instance checks if the first parameter is an instance of the second
        assert isinstance(animal, Animal)
        self.animals.append(animal)
    
    def remove_pet(self, animal):
        try:
            self.animals.remove(animal)
        except:
            print("No such animal. ")
        else:
            print(f"{animal} removed. ")
    
    def feature(self, name):
        for pet in self.animals:
            if pet.name == name:
                self.featured_pet = pet
                print(f"Featured pet is . . . {pet}")
                break
        else:
            print("There is no such pet. ")
    
    def get_featured(self):
        return self.featured_pet
    
    def feed(self):
        for pet in self.animals:
            pet.eat()
    
    def get_mammals(self):
        return self.get_by_type(Mammal)
    
    def get_reptiles(self):
        return self.get_by_type(Reptile)
    
    def get_birds(self):
        return self.get_by_type(Bird)
    
    def get_fish(self):
        return self.get_by_type(Fish)
    
    def get_by_type(self,typ):
        return [pet for pet in self.animals if isinstance(pet, typ)]


class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is {self.name}. "
    
    def eat(self):
        print(f"{self.name} is eating {self.diet}. ")

class Mammal(Animal):
    pass

class Cat(Mammal):
    def __init__(self, name, diet):
        super().__init__(name)
        self.diet = diet
    diet = "mice"

class Dog(Mammal):
    diet = "kibble"

class Reptile(Animal):
    pass

class Snake(Reptile):
    diet = "rodents"

class Turtle(Reptile):
    diet = "carrots"

class Bird(Animal):
    pass

class Parakeet(Bird):
    diet = "seeds"

class Toucan(Bird):
    diet = "caterpillars"

class Amphiban(Animal):
    pass

class Frog(Amphiban):
    diet = "flies"

class Newt(Amphiban):
    diet = "worms"

class Fish(Animal):
    pass

class Koi(Fish):
    diet = "algae"

class Guppy(Fish):
    diet = "flakes"


store = PetStore(14405)
store.add_pet(Turtle("Tracy"))
store.add_pet(Cat("Catalina"))
store.add_pet(Turtle("Flash"))
store.add_pet(Snake("Robbin"))
store.add_pet(Dog("Woofface"))
store.add_pet(Parakeet("Kra"))
store.add_pet(Newt("Newtace"))
store.add_pet(Koi("Ssunsett"))

store.feed()
store.feature("Catalina")

print("Fish: ")
for pet in store.get_fish():
    print(pet)

