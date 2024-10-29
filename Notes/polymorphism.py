#polymorphism: unction or methods can do multiple things based on the inputs
#"You are never done with libraries" - LaRose
#"And it's not gonna say anything cause I'm not trying to do anything with it yet. " - LaRose
#"You're not real" - Ethan
#"How old do you think shape is? " - LaRose
#"This is to protect your code from stupid people. " - LaRose
#"Find your calm, children. " - LaRose
#

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x):
        self.x = x

    @abstractmethod
    def area(self, x):
        return 0

class Square(Shape):
    def area(self):
        return self.x * self.x

class Circle(Shape):
    def area(self):
        return round((self.x ** 2 * math.pi), 2)

class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    
    def area(self):
        return self.x * self.y

# sqr = Square(4)
# cir = Circle(4)
# rec = Rectangle(5, 3)
# print(sqr.area())
# print(cir.area())
# print(rec.area())

shapes = [Square(4), Circle(4), Rectangle(5, 3), "Tts", Rectangle(8, 2)]

for shape in shapes:
    if isinstance(shape, Shape):
        print(shape.area())