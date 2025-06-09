from src.math_op import add,sub,mul,div

def test_add():
    assert add(1,2) == 3
    assert add(3,2) == 5
    assert add(4,2) == 6

def test_sub():
    assert sub(1,2) == -1
    assert sub(3,2) == 1
    assert sub(4,2) == 2

def test_mul():
    assert mul(1,2) == 2
    assert mul(3,2) == 6
    assert mul(4,2) == 8

def test_div():
    assert div(2,2) == 1
    assert div(10,2) == 5
    assert div(30,3) == 10

