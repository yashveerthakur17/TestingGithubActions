from src.math_op import add,sub,mul,div

def test_add():
    assert add(1,2) == 3
    assert add(3,2) == 4
    assert add(4,2) == 5

def test_sub():
    assert sub(1,2) == 3
    assert sub(3,2) == 4
    assert sub(4,2) == 5

def test_mul():
    assert mul(1,2) == 3
    assert mul(3,2) == 4
    assert mul(4,2) == 5

def test_div():
    assert div(1,2) == 3
    assert div(3,2) == 4
    assert div(4,2) == 5

