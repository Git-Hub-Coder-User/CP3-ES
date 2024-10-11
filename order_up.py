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
    Checks to see if ordered items are on the menu (Tells user if what they ordered isn't on the menu)
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
    Method to calculate total - Done! Tax? 
    Decision structure that autofills none if the user doesn't want anything in the category - Not used (The second half) - Done! 
    Bonus: 
        World building
        Create default orders - Done! 
"""

class Order:

    menu = {"water": 1.49, "soda": 5.99, "juice": 3.99, "fries": 4.99, "watermelon": 3.99, "stringbeans": 2.99, "salad": 6.99, "burger": 5.99, "soup": 6.99, "chicken nuggets": 3.99, "slurpables": 3.49, "rice": 1.99, "cake": 6.99, "cookies": 2.99, "pie": 4.99}

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
        if self.drink == None and self.appetizer == None and self.main == None and self.side1 == None and self.side1 == None and self.dessert == None:
            return True
        else:
            return False
    
    def change_item(self, item):
        replacement = input("What would you like? ").strip().lower()
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
        total = 0
        for item in self.create_list():
            total += self.menu[item]
        return total

    @staticmethod
    def in_menu(item):
        if not item.strip().lower() in Order.menu:
            return False
        else:
            return True
    
    @classmethod
    def classic(self):
        return Order("soda", "watermelon", "burger", "fries", None, "cookies")
    @classmethod
    def special(self):
        order = Order("soda", "watermelon", "burger", "fries", "slurpables", None)
        print("For the dessert, you need to choose a dessert! ")
        order.change_item("dessert")
        return order
        
def get_order(order):

    order = order

    while True:

        inputed = input("Would you like the classic, the special, or to choose your own order? \n")

        if "cl" in inputed:
            order = Order.classic()
        elif "sp" in inputed:
            order = Order.special()
        else: 
            while True: 
                inputed = input("Would you like a drink? ").strip().lower()
                if "y" in inputed: 
                    order.change_item("drink")
                    break
                elif "n" in inputed:
                    break
                else:
                    print("Invalid option")
            while True: 
                inputed = input("Would you like an appetizer? ").strip().lower()
                if "y" in inputed: 
                    order.change_item("appetizer")
                    break
                elif "n" in inputed:
                    break
                else:
                    print("Invalid option")
            while True: 
                inputed = input("Would you like a main dish? ").strip().lower()
                if "y" in inputed: 
                    order.change_item("main")
                    break
                elif "n" in inputed:
                    break
                else:
                    print("Invalid option")
            while True: 
                inputed = input("Would you like a side? ").strip().lower()
                if "y" in inputed: 
                    order.change_item("side1")
                    while True:
                        inputed = input("Would you like a second side? ").strip().lower()
                        if "y" in inputed:
                            order.change_item("side2")
                        elif "n" in inputed:
                            break
                        else:
                            print("Invalid option. ")
                        break
                elif "n" in inputed:
                    break
                else:
                    print("Invalid option")
                break
            while True: 
                inputed = input("Would you like a dessert? ").strip().lower()
                if "y" in inputed: 
                    order.change_item("dessert")
                    break
                elif "n" in inputed:
                    break
                else:
                    print("Invalid option")

        # break

        if order.is_empty():
            print("Your order is empty. Please try again, \n")
        else: 
            print(order)
            print(f"Your total is {order.total():.2f}\n")
            return order

        
order = Order()
order = get_order(order)
inputed = ""

while True: 
    if inputed != "Try again. ":
        inputed = input("Is your order correct? \n")

    if "y" in inputed:
        break
    elif "n" in inputed or "Try again" == inputed:
        inputed = input("What part is incorrect? \n")
        if "drink" in inputed:
            order.change_item("drink")
        elif "appetizer" in inputed:
            order.change_item("appetizer")
        elif "main" in inputed:
            order.change_item("main")
        elif "side" in inputed and "1" in inputed or "first" in inputed:
            order.change_item("side1")
        elif "side" in inputed and "2" in inputed or "second" in inputed:
            order.change_item("side2")
        elif "dessert" in inputed:
            order.change_item("dessert")
        else:
            print("Invalid option. ")
            inputed = "Try again"
    else: 
        print("Invalid option. ")
    
    print(order)