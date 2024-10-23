from equations import(
    add,
    sub,
    multi,
    div
)

def test_add():
    assert add(2, 10) == 12
    assert add(3, 5) == 8
    assert add(4, 6) == 10

def test_sub():
    assert sub(2, 10) == -8
    assert sub(3, 5) == -2
    assert sub(4, 6) == -2

def test_multi():
    assert multi(2, 10) == 20
    assert multi(3, 5) == 15
    assert multi(4, 6) == 24

def test_div():
    assert div(2, 10) == .2
    assert div(3, 5) == .6
    assert div(4, 6) == 2/3