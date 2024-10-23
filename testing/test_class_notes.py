from class_notes import Animal

def test_get_name():
    testanimal = Animal("PikaPika", "Bobcat", 3, "Female", "Epic")
    name = testanimal.get_name()
    assert name == "PikaPika"