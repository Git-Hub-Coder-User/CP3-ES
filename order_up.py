"""
Create a program that uses a class to take an order at a diner. 

 

The class for the order needs to have space for
    A drink
    An appetizer 
    A main course
    Two sides
    A dessert
    Please note that the user doesn't have to order an item for each category, they just need to be given the option

The class needs to have methods that
    Prints out everything the user has ordered
    Gives the user a total for their order 
    Checks to see if ordered items are on the men (Tells user if what they ordered isn't on the menu)
    Makes sure that the user has ordered at least 1 item
    Allows user to place their order 
    Allows user to change an item in their order
"""
"""
To-do: 
    Create menu
    Create class for the order with default None (print statement will need to skip the Nones) - No, decision structure does the default none
    Create function to check to see if ordered item is in menu
    Method for making sure order is not empty
    Method to change items 
    Method to calculate total
    Decision structure that autofills none if the user doesn't want anything in the category
    World building
"""

class Order:
    def __init__(self, drink, appetizer, main, side1, side2, dessert):
        self.drink = drink
        self.appetizer = appetizer
        self.main = main
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert

order = Order("Water", "fries", )