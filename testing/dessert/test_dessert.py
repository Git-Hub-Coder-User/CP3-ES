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

def test_DessertItem():
    item1 = DessertItem("Pie")
    item2 = DessertItem("Cake")
    item3 = DessertItem("Cakepop")
    assert item1.name == "Pie"
    assert item2.name == "Cake"
    assert item3.name == "Cakepop"
    
def test_DessertItem():
    item1 = DessertItem("Pie")
    item2 = DessertItem("Cake")
    item3 = DessertItem("Cakepop")
    assert item1.name == "Pie"
    assert item2.name == "Cake"
    assert item3.name == "Cakepop"


def test_DessertItem():
    item1 = DessertItem("Pie")
    item2 = DessertItem("Cake")
    item3 = DessertItem("Cakepop")
    assert item1.name == "Pie"
    assert item2.name == "Cake"
    assert item3.name == "Cakepop"