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
    Create menu - Done! 
    Create class for the order with default None (print statement will need to skip the Nones) - No, decision structure does the default none - or maybe not so I can just use  
        the change method - Done! 
    Create function/method to check to see if ordered item is in menu - Done! 
    Method for making sure order is not empty - Done! 
    Method to change items - Done! 
    Method to calculate total
    Decision structure that autofills none if the user doesn't want anything in the category - Not used
    World building
"""

class Order:

    menu = {"water": 1.50, "soda": 5.00, "juice": 3.00, "fries": 4.00, "watermelon": 3.00, "stringbeans": 2.00, "salad": 6.00, "burger": 5.00, "soup": 6.00, "chicken nuggets": 3.00, "slurpables": 3.50, "rice": 1.00, "cake": 6.00, "cookie": 2.00, "pie": 4.00}

    def __init__(self = None, drink = None, appetizer = None, main = None, side1 = None, side2 = None, dessert = None):
        self.drink = drink
        self.appetizer = appetizer
        self.main = main
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert
    
    def __str__(self):
        string = "Your order is: "
        if self.drink != None:
            string += f"{self.drink.strip().lower().capitalize()}, "
        if self.appetizer != None:
            string += f"{self.appetizer.lower().capitalize()}, "
        if self.main != None:
            string += f"{self.main.lower().capitalize()}, "
        if self.side1 != None:
            string += f"{self.side1.lower().capitalize()}, "
        if self.side2 != None:
            string += f"{self.side2.lower().capitalize()}, "
        if self.dessert != None:
            string += f"{self.dessert.lower().capitalize()}, "
        
        string = string[:-2]
        return(string)
    
    def create_list(self):
        listed = [self.drink, self.appetizer, self.main, self.side1, self.side2, self.dessert]
        while None in listed:
            listed.remove(None)
        return listed

    def is_empty(self):
        if str(self).count(None) == 6:
            return True
        else:
            return False
    
    def change_item(self, item):
        replacement = input("What would you like instead? ").strip().lower()
        while not self.in_menu(replacement):
            print(f"I'm sorry. {replacement.capitalize()} is not in the menu. ")
            replacement = input("What would you like instead? ")
        while True: 
            if item == "drink":
                self.drink = replacement
            elif item == "appetizer":
                self.appetizer = replacement
            elif item == "main":
                self.main = replacement
            elif item == "side1":
                self.side1 = replacement
            elif item == "side2":
                self.side2 = replacement
            elif item == "dessert":
                self.dessert = replacement
            else:
                print(f"I'm sorry, {item} is not a category. ")
                item = input("Please select another category. ")
                continue
            break
    
    def total(self):
        pass
    @staticmethod
    def in_menu(item):
        if not item.strip().lower() in Order.menu:
            return False
        else:
            return True
        

order = Order("water", "fries")
print(order)
print(order.create_list())