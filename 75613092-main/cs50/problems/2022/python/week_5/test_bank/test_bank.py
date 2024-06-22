from bank import value

def test_one():
    assert value("HELLO") == 0
    assert value("HEY") == 20
    assert value("CAT") == 100

def test_two():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("cat") == 100

def test_three():
    assert value("What in the cat") == 100
