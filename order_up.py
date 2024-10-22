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
    Method to calculate total - Done! Tax? - Added! 
    Decision structure that autofills none if the user doesn't want anything in the category - Not used (The second half) - Done! 
    Bonus: 
        World building - Good enough
        Create default orders - Done! 
"""

class Order:

    menu = {"water": 1.49, "soda": 5.99, "juice": 3.99, "fries": 4.99, "watermelon": 3.99, "stringbeans": 2.99, "salad": 6.99, "burger": 5.99, "soup": 6.99, "chicken nuggets": 3.99, "slurpables": 3.49, "rice": 1.99, "cake": 6.99, "cookies": 2.99, "pie": 4.99}
    drink_menu = ["water", "soda", "juice"]
    appetizer_menu = ["fries", "watermelon", "stringbeans"]
    main_menu = ["salad", "burger", "soup"]
    side_menu = ["chicken nuggets", "slurpables", "rice"]
    dessert_menu = ["cake", "cookies", "pie"]

    def __init__(self = None, drink = None, appetizer = None, main = None, side1 = None, side2 = None, dessert = None):
        self.drink = drink
        self.appetizer = appetizer
        self.main = main
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert
    
    def __str__(self):
        string = "\nYour order is: "
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
    
    #Makes a list form of the Order so it's easier to deal with
    def create_list(self):
        listed = [self.drink, self.appetizer, self.main, self.side1, self.side2, self.dessert]
        while None in listed:
            listed.remove(None)
        for value in listed:
            listed[listed.index(value)] = value.strip().lower()
        return listed

    #Checks if order is empty
    def is_empty(self):
        if self.drink == None and self.appetizer == None and self.main == None and self.side1 == None and self.side1 == None and self.dessert == None:
            return True
        else:
            return False
    
    #Lets user change item, also used to create the order
    def change_item(self, item):
        replacement = input("What would you like? ").strip().lower()
        print(item) ###
        while not self.in_menu(replacement, item):
            print(f"I'm sorry. {replacement.capitalize()} is not in that menu. ")
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
    
    #Gets total
    def total(self):
        total = 0
        for item in self.create_list():
            total += self.menu[item]
        return total

    @staticmethod
    #Checks if item is menu
    def in_menu(item, group):
        # print("In menu called")
        if not item.strip().lower() in Order.menu:
            # print("THIS LINE RAN")
            return False
        elif group == "drink":
            if item not in Order.drink_menu:
                print("I ran! ")
                return False
        elif group == "appetizer":
            if item not in Order.appetizer_menu:
                return False
        elif group == "main":
            if item not in Order.main_menu:
                return False
        elif group == "side":
            if item not in Order.side_menu:
                return False
        elif group == "dessert":
            if item not in Order.dessert_menu:
                return False
        # print("I ran")
        return True
    
    #Starter orders
    @classmethod
    def classic(self):
        return Order("soda", "watermelon", "burger", "fries", None, "cookies")
    @classmethod
    def special(self):
        order = Order("soda", "watermelon", "burger", "fries", "slurpables", None)
        print("For the special, you need to choose a dessert! ")
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
                    print("Invalid option. ")
            while True: 
                inputed = input("Would you like an appetizer? ").strip().lower()
                if "y" in inputed: 
                    order.change_item("appetizer")
                    break
                elif "n" in inputed:
                    break
                else:
                    print("Invalid option. ")
            while True: 
                inputed = input("Would you like a main dish? ").strip().lower()
                if "y" in inputed: 
                    order.change_item("main")
                    break
                elif "n" in inputed:
                    break
                else:
                    print("Invalid option. ")
            while True: 
                inputed = input("Would you like a side? ").strip().lower()
                if "y" in inputed: 
                    order.change_item("side1")
                    while True:
                        inputed = input("Would you like a second side? ").strip().lower()
                        if "y" in inputed:
                            order.change_item("side2")
                            break
                        elif "n" in inputed:
                            break
                        else:
                            print("Invalid option. ")
                elif "n" in inputed:
                    break
                else:
                    print("Invalid option. ")
                break
            while True: 
                inputed = input("Would you like a dessert? ").strip().lower()
                if "y" in inputed: 
                    order.change_item("dessert")
                    break
                elif "n" in inputed:
                    break
                else:
                    print("Invalid option. ")

        # break

        if order.is_empty():
            print("Your order is empty. Please try again, \n")
        else: 
            print(order)
            print(f"Your pre-tax total is {order.total():.2f}. Tax is {(order.total() * .02):.2f}. Your total is {(order.total() * 1.02):.2f}\n")
            return order


import random

order = Order()
inputed = ""
bank_account_total = random.randint(100, 5000)
bank_account_total /= 100


for i in range(1): #I'm putting this in a loop to make the code a bit more readable. This loop prints the options
    print(f"\nBefore entering the restaraunt, you check your bank account to find you have {bank_account_total} dollars in your account. \n\n")
    print("Hello, and welcome to the Dia's! We're happy to have you here! What can I get for you today? ")
    print("Our menu, while always growing, is as follows. \n\tFor drinks you can have water for 1.49, soda for 5.99, or juice for 3.99. \n\tAs an appetizer, you can have fries for 4.99, watermelon for 3.99, or stringbeans for 2.99. \n\tFor our main dishes we're proud to offer salad for 6.99, a burger for 5.99, and soup for 6.99. \n\tOur avaiable sides are chicken nuggets for 3.99, slurpables for 3.49, and rice for 1.49. \n\tFinally, our desserts are cake for 6.99, cookies for 2.99, and pie for 4.99. \n")
    print("We also have two starter orders just to make life easier for you. \n\tThe classic has a soda as a drink, watermelon as an appetizer, a burger as the main dish, fries as the side, and cookies for dessert. \n\tThe special has a soda as a drink, watermelon as the side, a burger as the main dish, fries as one side and slurpables as the other. Then you get to choose a dessert! \n")



order = get_order(order)

while True: 
    if inputed != "Try again. ":
        inputed = input("Is your order correct? ")

    if "y" in inputed:
        break
    elif "n" in inputed or "Try again" == inputed:
        inputed = input("What part is incorrect? ")
        if "drink" in inputed:
            order.change_item("drink")
        elif "appetizer" in inputed:
            order.change_item("appetizer")
        elif "main" in inputed:
            order.change_item("main")
        elif ("side" in inputed) and ("1" in inputed or "first" in inputed or "2" not in inputed or "second" not in inputed):
            # print("This part ran for some reason")
            # print("side" in inputed)
            order.change_item("side1")
        elif "side" in inputed and "2" in inputed or "second" in inputed:
            order.change_item("side2")
        elif "dessert" in inputed:
            # print("I RAN")
            order.change_item("dessert")
        else:
            print("Invalid option. \n")
            inputed = "Try again"
    else: 
        print("Invalid option. \n")
    
    print(order)
    print(f"Your pre-tax total is {order.total():.2f}. Tax is {(order.total() * .02):.2f}. Your total is {(order.total() * 1.02):.2f}\n")

if bank_account_total < order.total():
    print("\nWhen you try to pay for your meal, you hear a beep and you look down to see red letters spelling out 'Credit Card Declined'. The cashier gives you a judgemental look and you shrink away. After a quick glance around, you bolt out of the restaraunt, embarassed. \n\nNext time, pay more attention to how much money you have. ")
else: 
    print("\nThank you for coming! We hope that you'll enjoy your food and we'll see you again soon! \n")