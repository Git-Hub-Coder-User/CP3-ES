from dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

class Order():
    def __init__(self):
        self.order = []

    def __str__(self):
        string = ""
        for value in self.order:
            string += value.name + "\n"

        return string
    
    def __len__(self):
        return len(self.order)
    
    def add(self, DessertItem):
        self.order.append(DessertItem)
        return self.order

def main():
    order = Order()
    order.add(Candy("Candy Corn", 1.5, .25))
    order.add(Candy("Gummy Bears", .25, .35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, .79))
    order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    print(order, end = "")
    print("Total number of items in order:", len(order))

main()
