"""
'A Dessert Shop sells candy by the pound, cookies by the dozen, ice cream by the scoop, and sundaes (ice cream with a topping).
For this part of the project, you will create the structure for a Dessert Shop program. There will be no user interface nor input/output at this time, but there will be later. Your code will be tested using automated test cases.
Test code can be simple asserts, unittest code, pytest code, or doctests as long as your set of test cases meets the requirements specified for the project. Whichever you choose, be consistent. unittest is built-in with Python, as are doctests and asserts. pytest is a 3rd-party module but is simpler to write code for than unittest, and it will run unittest code. Whichever you choose, be consistent.
To create this framework, you will implement an inheritance hierarchy of classes derived from a DessertItem superclass. Candy, Cookie, and IceCream classes will derive from the DessertItem class. The Sundae class will derive from the IceCream class. The classes will be structured as below.' - Instructions

"""

class DessertItem():
    def __init__(self, name = ""):
        self.name = name


class Candy(DessertItem):
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

class Cookie(DessertItem):
    def __init__(self, name, quantity = 0, price_per_dozen = 0.0):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen

class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

class Sundae(IceCream):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0, topping_name = "", topping_price = 0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price