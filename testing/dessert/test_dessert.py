from testing.dessert.dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)

def test_DessertItem():
    item1 = DessertItem("Pie")
    item2 = DessertItem("Cake")
    item3 = DessertItem("Cakepop")
    assert item1.name == "Pie"
    assert item2.name == "Cake"
    assert item3.name == "Cakepop"

def test_Candy():
    item1 = Candy("Lollipop")
    item2 = Candy("Slurpables")
    item3 = Candy("Skittles")
    assert item1.name == "Lollipop"
    assert item2.name == "Slurpables"
    assert item3.name == "Skittles"

def test_Cookie():
    item1 = Cookie("Chocolate chip cookies")
    item2 = Cookie("Blondie bites")
    item3 = Cookie("Lemon cookies")
    assert item1.name == "Chocolate chip cookies"
    assert item2.name == "Blondie bites"
    assert item3.name == "Lemon cookies"
    
def test_IceCream():
    item1 = IceCream("Vanilla")
    item2 = IceCream("Chocolate")
    item3 = IceCream("Mint")
    assert item1.name == "Vanilla"
    assert item2.name == "Chocolate"
    assert item3.name == "Mint"


def test_Sundae():
    item1 = Sundae("Vanilla")
    item2 = Sundae("Chocolate")
    item3 = Sundae("Strawberry")
    assert item1.name == "Vanilla"
    assert item2.name == "Chocolate"
    assert item3.name == "Strawberry"